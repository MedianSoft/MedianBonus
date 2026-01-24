import { useState, useEffect } from 'react';
import { Modal } from '@/shared/ui/Modal/Modal';
import type { Employee } from '@/shared/types/employee';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  onSave: (data: any) => void;
  loading: boolean;
  initialData?: Employee | null; // Добавили данные для редактирования
}

export const EmployeeModal = ({ isOpen, onClose, onSave, loading, initialData }: Props) => {
  const [form, setForm] = useState({ name: '', email: '', password: '' });

  // Синхронизируем форму с входящими данными при открытии
  useEffect(() => {
    if (isOpen) {
      if (initialData) {
        // Если редактируем: заполняем поля, пароль оставляем пустым
        setForm({
          name: initialData.name,
          email: initialData.email,
          password: '',
        });
      } else {
        // Если создаем нового: очищаем поля
        setForm({ name: '', email: '', password: '' });
      }
    }
  }, [initialData, isOpen]);

  // Проверка валидности (пароль обязателен только при создании)
  const isFormInvalid = !form.name || !form.email || (!initialData && !form.password);

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={initialData ? "Редактировать сотрудника" : "Добавить сотрудника"}
    >
      <div className="space-y-4">
        {/* Поле ФИО */}
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-gray-400 ml-1">ФИО сотрудника</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-all"
            placeholder="Иван Иванов"
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
          />
        </div>

        {/* Поле Email */}
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-gray-400 ml-1">Электронная почта</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-all"
            placeholder="example@mail.com"
            type="email"
            value={form.email}
            onChange={e => setForm({...form, email: e.target.value})}
          />
        </div>

        {/* Поле Пароль — показываем только при создании или если нужно сменить */}
        {!initialData && (
          <div className="space-y-1.5">
            <label className="text-sm font-medium text-gray-400 ml-1">Пароль</label>
            <input
              className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-all"
              placeholder="••••••••"
              type="password"
              value={form.password}
              onChange={e => setForm({...form, password: e.target.value})}
            />
          </div>
        )}
      </div>

      <div className="flex flex-col gap-3 mt-8">
        <button
          onClick={() => onSave(form)}
          disabled={loading || isFormInvalid}
          className="w-full bg-orange-500 hover:bg-orange-600 py-3 rounded-xl text-white font-bold disabled:opacity-50 transition-all active:scale-[0.98]"
        >
          {loading ? 'Сохранение...' : initialData ? 'Сохранить изменения' : 'Создать'}
        </button>
        <button
          onClick={onClose}
          className="w-full text-gray-500 hover:text-white py-2 transition-colors text-sm"
        >
          Отмена
        </button>
      </div>
    </Modal>
  );
};
