import { useState, useEffect } from 'react';
import type { Employee } from '@/shared/types/employee';
import { employeeApi } from '@/shared/api/employee';

export function useEmployees(notify: any) {
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
      let response;
      if (currentEmployee?.id) {
        response = await employeeApi.update({ ...formData, id: currentEmployee.id });
      } else {
        response = await employeeApi.create({ ...formData, business_id: currentBusinessId });
      }

      // В fetch нужно проверять response.ok (статус 200-299)
      if (response.ok) {
        await loadEmployees();
        closeModal();
        // ВЫЗОВ УВЕДОМЛЕНИЯ
        notify.showSuccess(
          currentEmployee?.id
            ? "Данные сотрудника успешно обновлены"
            : "Новый сотрудник успешно зарегистрирован"
        );
      } else {
        // Если бэк прислал ошибку (например 422)
        notify.showError("Не удалось сохранить данные. Проверьте правильность заполнения полей.");
      }
    } catch (e) {
      notify.showError("Ошибка соединения с сервером. Попробуйте позже.");
      console.error(e);
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
      const response = await employeeApi.delete(id);

      if (response.ok) {
        setEmployees(prev => prev.filter(emp => emp.id !== id));
        notify.showSuccess("Сотрудник удален из системы");
      } else {
        notify.showError("Не удалось удалить сотрудника");
      }
    } catch (e) {
      notify.showError("Ошибка при выполнении запроса");
    }
  };

  useEffect(() => { loadEmployees(); }, []);

  return {
    employees,
    isModalOpen,
    isLoading,
    currentEmployee,
    setIsModalOpen,
    openCreateModal,
    openEditModal,
    closeModal,
    handleSave,
    removeEmployee,
    loadEmployees
  };
}
