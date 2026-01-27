import { useState, useEffect } from 'react';
import { customerApi } from '@/shared/api/customer';
import type { Customer } from '@/shared/types/customer';

export function useCustomers(notify: any) {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [currentCustomer, setCurrentCustomer] = useState<Customer | null>(null);
  const [searchLoading, setSearchLoading] = useState(false);

  const openCreateModal = () => {
    setCurrentCustomer(null); // Сбрасываем, чтобы форма была чистой
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentCustomer(null);
  };

  const findByPhone = async (phone: string) => {
    setSearchLoading(true);
    try {
      const customer = await customerApi.getByPhone(phone);
      // Если нашли — можно либо выделить его в списке, либо открыть модалку на редактирование
      openEditModal(customer);
    } catch (e) {
      notify.showError("Клиент с таким номером не зарегистрирован");
    } finally {
      setSearchLoading(false);
    }
  };

  const loadCustomers = async () => {
    try {
      const data = await customerApi.getAll();
      setCustomers(Array.isArray(data) ? data : (data as any).customers || []);
    } catch (e) {
      console.error(e);
    }
  };

  const loadCustomerById = async (id: string) => {
    setIsLoading(true);
    try {
      const customer = await customerApi.getById(id);
      // Например, сразу открываем модалку с полученными данными
      openEditModal(customer);
    } catch (e) {
       notify.showError("Не удалось загрузить данные клиента");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSave = async (formData: any) => {
    setIsLoading(true);
    try {
      let response;
      if (currentCustomer?.id) {
        response = await customerApi.update({ ...formData, id: currentCustomer.id });
      } else {
        response = await customerApi.create(formData);
      }

      // 4. Проверяем response.ok (если ваш API возвращает стандартный fetch response)
      // Если API возвращает сразу данные, используйте просто try/catch
      if (response && (response.ok || response.id)) {
        await loadCustomers();
        closeModal();
        // 5. Вызов уведомления об успехе
        notify.showSuccess(
          currentCustomer?.id
            ? "Данные клиента успешно обновлены"
            : "Новый клиент успешно зарегистрирован"
        );
      } else {
        notify.showError("Не удалось сохранить данные. Проверьте поля формы.");
      }
    } catch (e) {
      // 6. Уведомление при ошибке сети/сервера
      notify.showError("Ошибка сохранения. Попробуйте позже.");
      console.error(e);
    } finally {
      setIsLoading(false);
    }
  };

  const openEditModal = (customer: Customer) => {
    setCurrentCustomer(customer);
    setIsModalOpen(true);
  };

  useEffect(() => { loadCustomers(); }, []);

  return {
    customers,
    isModalOpen,
    setIsModalOpen,
    isLoading,
    handleSave,
    openEditModal,
    currentCustomer,
    setCurrentCustomer,
    findByPhone,
    searchLoading,
    loadCustomerById,
    openCreateModal,
    closeModal
  };
}
