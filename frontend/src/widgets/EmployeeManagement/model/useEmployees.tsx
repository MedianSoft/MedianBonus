import { useState, useEffect } from 'react';
import type { Employee } from '@/shared/types/employee';
import { employeeApi } from '@/shared/api/employee';

export function useEmployees() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [currentEmployee, setCurrentEmployee] = useState<Employee | null>(null);

  const currentBusinessId = "3fa85f64-5717-4562-b3fc-2c963f66afa6";

  const loadEmployees = async () => {
    try {
      const data = await employeeApi.getAll();
      setEmployees(data.employees || []);
    } catch (e) {
      console.error("Ошибка загрузки:", e);
    }
  };

  const handleSave = async (formData: any) => {
    setIsLoading(true);
    try {
      if (currentEmployee?.id) {
        // Редактирование
        await employeeApi.update({ ...formData, id: currentEmployee.id });
      } else {
        // Создание
        await employeeApi.create({ ...formData, business_id: currentBusinessId });
      }
      await loadEmployees();
      closeModal();
    } catch (e) {
      alert("Ошибка при сохранении данных");
    } finally {
      setIsLoading(false);
    }
  };

  // ЭТА ФУНКЦИЯ ДЛЯ КНОПКИ "+" (Новый сотрудник)
  const openCreateModal = () => {
    setCurrentEmployee(null); // Очищаем, чтобы форма была пустой
    setIsModalOpen(true);
  };

  // ЭТА ФУНКЦИЯ ДЛЯ КНОПКИ "Изменить"
  const openEditModal = (employee: Employee) => {
    setCurrentEmployee(employee); // Заполняем данными сотрудника
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentEmployee(null);
  };

  const removeEmployee = async (id: string) => {
    if (!confirm('Вы уверены?')) return;
    try {
      await employeeApi.delete(id);
      setEmployees(prev => prev.filter(emp => emp.id !== id));
    } catch (e) {
      alert("Ошибка при удалении");
    }
  };

  useEffect(() => { loadEmployees(); }, []);

  return {
    employees,
    isModalOpen,
    isLoading,
    currentEmployee,
    setIsModalOpen,
    openCreateModal, // Добавил обратно
    openEditModal,
    closeModal,
    handleSave,
    removeEmployee,
    loadEmployees
  };
}
