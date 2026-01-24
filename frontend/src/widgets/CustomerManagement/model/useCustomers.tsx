import { useState, useEffect } from 'react';
import { customerApi } from '@/shared/api/customer';
import type { Customer } from '@/shared/types/customer';

export function useCustomers() {
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
      alert("Клиент с таким номером не зарегистрирован");
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
      alert("Не удалось загрузить данные клиента");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSave = async (formData: any) => {
    setIsLoading(true);
    try {
      if (currentCustomer?.id) {
        // PATCH если редактируем
        await customerApi.update({ ...formData, id: currentCustomer.id });
      } else {
        // POST если создаем
        await customerApi.create(formData);
      }
      await loadCustomers();
      setIsModalOpen(false);
      setCurrentCustomer(null);
    } catch (e) {
      alert("Ошибка при сохранении");
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
