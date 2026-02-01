# 🏆 Median Bonus
Система управления бонусами и активностями. Проект разделен на независимые Frontend и Backend части.
## 📂 Структура проекта
```text
median-bonus/
├── backend/                # Серверная часть (Python/FastAPI)
│   ├── main.py             # Точка входа в приложение
│   └── api/                # Эндпоинты API
│
├── frontend/               # Клиентская часть (React + Vite + TS)
│   ├── src/
│   │   ├── app/            # Инициализация (роутинг, провайдеры)
│   │   │   ├── App.tsx
│   │   │   └── router.tsx
│   │   ├── pages/          # Страницы приложения
│   │   │   ├── dashboard/  # Главный экран
│   │   │   ├── auth/       # Вход / Регистрация
│   │   │   └── admin/      # Панель администратора
│   │   ├── widgets/        # Крупные блоки (Stats, Lists)
│   │   ├── shared/         # Общие компоненты и UI-кит
│   │   ├── main.tsx
│   │   └── index.css       # Tailwind стили
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── docker-compose.yml      # Оркестрация контейнеров
└── pyproject.toml          # Зависимости и конфиг
```
## Первый запуск сервиса:
1. ```cp .env.example .env```
2. ```docker compose up```

## Установка линтеров:
1. ```lefthook install```

## Генерация ревизии Alembic:
1. ```docker exec -it backend alembic revision --autogenerate```