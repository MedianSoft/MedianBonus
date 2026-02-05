from typing import TYPE_CHECKING

from app.domain.bonus import BonusType
from app.domain.customer import Customer
from app.domain.customer_bonus import CustomerBonus
from app.domain.order import Order, OrderProduct
from app.domain.product import Product
from app.schema.order import OrderProductRequest, OrderRequest, OrderResponse
from app.util.exception_handler import NotFoundError

if TYPE_CHECKING:
    from app.domain.bonus import BonusRepository
    from app.domain.customer import CustomerRepository
    from app.domain.customer_bonus import CustomerBonusRepository
    from app.domain.order import OrderProductRepository, OrderRepository
    from app.domain.product import ProductRepository


class OrderService:
    def __init__(
        self,
        order_repository: "OrderRepository",
        order_product_repository: "OrderProductRepository",
        bonus_repository: "BonusRepository",
        product_repository: "ProductRepository",
        customer_bonus_repository: "CustomerBonusRepository",
        customer_repository: "CustomerRepository",
    ) -> None:
        self.order_repository = order_repository
        self.order_product_repository = order_product_repository
        self.bonus_repository = bonus_repository
        self.product_repository = product_repository
        self.customer_bonus_repository = customer_bonus_repository
        self.customer_repository = customer_repository

    async def create(self, data: "OrderRequest") -> OrderResponse:
        # Пользователь зарегистрирован?
        customer = None

        if data.customer_phone:
            customer = await self.customer_repository.get_by_phone(phone=data.customer_phone)

        if not customer:
            customer = await self.customer_repository.create(Customer(phone=data.customer_phone))

        order = Order(
            store_id=data.store_id,
            customer_id=customer.id if customer else None,
            price=0,
            price_with_discount=0,
            points_spend=0,
            points_earned=0,
        )
        gift = None

        items: list[OrderProduct] = []
        for req in data.products:
            product = await self.product_repository.get(model=Product, id=req.product_id)
            if not product:
                raise NotFoundError("Product")

            order_product = OrderProduct(
                product_id=req.product_id,
                price=product.price,
                quantity=req.quantity,
            )

            items.append(order_product)
            order.price += order_product.price * order_product.quantity

        if customer:
            # Узнаем, какие бонусы есть в магазине
            bonuses = await self.bonus_repository.get_all_by_store(store_id=data.store_id)
            for bonus in bonuses:
                # Скидки
                if bonus.type == BonusType.DISCOUNT:
                    for item in items:
                        if item.product_id == bonus.product_id:
                            # Снижаем цену на товар со скидкой
                            item.price *= 1 - (bonus.value / 100)
                        order.price_with_discount += item.price * item.quantity

                # Купи N товара -- получи 1 бесплатно
                if bonus.type == BonusType.GIFT:
                    # Клиент участвует в бонусной программе?
                    bonus_exists = await self.customer_bonus_repository.get_by_customer_and_bonus(
                        customer_id=customer.id, bonus_id=bonus.id
                    )

                    # Если не участвует
                    if not bonus_exists:
                        # Делаем так, чтобы участвовал
                        bonus_exists = CustomerBonus(
                            customer_id=customer.id,
                            bonus_id=bonus.id,
                            value=0,
                        )
                        _ = await self.customer_bonus_repository.create(bonus_exists)

                    # Если не накопил нужное кол-во покупок:
                    if bonus_exists.value < bonus.value:
                        # Но купил бонусный товар
                        for item in items:
                            if item.product_id == bonus.product_id:
                                # То добавляем 1 балл
                                bonus_exists.value += 1
                                break

                    # Если накопил нужное кол-во покупок
                    else:
                        # Добавляем этот товар в корзину с ценой = 0
                        gift = OrderProductRequest(
                            product_id=bonus.product_id,
                            quantity=1,
                        )
                        # И обнуляем бонусы
                        bonus_exists.value -= bonus.value

                # Баллы
                if bonus.type == BonusType.POINTS:
                    # Клиент участвует в бонусной программе?
                    bonus_exists = await self.customer_bonus_repository.get_by_customer_and_bonus(
                        customer_id=customer.id, bonus_id=bonus.id
                    )

                    # Если не участвует
                    if not bonus_exists:
                        # Делаем так, чтобы участвовал
                        bonus_exists = CustomerBonus(
                            customer_id=customer.id,
                            bonus_id=bonus.id,
                            value=bonus.value,
                        )
                        order.points_earned = bonus.value
                        _ = await self.customer_bonus_repository.create(bonus_exists)

                    # Если участвует и хочет копить баллы
                    elif not data.use_bonus:
                        # И купил бонусный товар
                        for item in items:
                            if item.product_id == bonus.product_id:
                                # То добавляем указанные в бонусе баллы, умноженные на кол-во товара
                                bonus_exists.value += bonus.value * item.quantity
                                break
                    # Если хочет списать баллы
                    else:
                        # сколько может потратить?
                        price_after_points = (
                            int(order.price_with_discount - bonus_exists.value)
                            if (order.price_with_discount - bonus.value > 0)
                            else 0
                        )
                        order.price_with_discount = price_after_points
                        bonus_exists.value = 0
                        order.points_spend = price_after_points

        order_product_responses = []
        for item in items:
            order_product_response = OrderProductRequest.model_validate(item)
            order_product_responses.append(order_product_response)
            order.price_with_discount += item.price * item.quantity

        result = await self.order_repository.create(order)

        order_response = OrderResponse(
            products=order_product_responses,
            price=result.price,
            price_with_discount=result.price_with_discount,
            points_spend=result.points_spend,
            points_earned=result.points_earned,
            gift=gift,
        )

        return order_response
