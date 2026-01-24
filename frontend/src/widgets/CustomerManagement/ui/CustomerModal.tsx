import { useState, useEffect } from 'react';
import { Modal } from '@/shared/ui/Modal/Modal';

export const CustomerModal = ({ isOpen, onClose, onSave, loading, initialData }: any) => {
  const [form, setForm] = useState({ name: '', phone: '' });

  // Когда открываем на редактирование, подставляем данные
  useEffect(() => {
    if (initialData) {
      setForm({ name: initialData.name, phone: initialData.phone });
    } else {
      setForm({ name: '', phone: '' });
    }
  }, [initialData, isOpen]);

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={initialData ? "Изменить клиента" : "Новый клиент"}>
      <div className="space-y-5">
        <div className="flex flex-col gap-1.5">
          <label className="text-xs font-semibold text-gray-500 uppercase">Имя клиента</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500"
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
          />
        </div>
        <div className="flex flex-col gap-1.5">
          <label className="text-xs font-semibold text-gray-500 uppercase">Телефон</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500"
            value={form.phone}
            onChange={e => setForm({...form, phone: e.target.value})}
          />
        </div>
      </div>
      <button
        onClick={() => onSave(form)}
        disabled={loading}
        className="w-full bg-orange-500 mt-8 py-3 rounded-xl text-white font-bold"
      >
        {loading ? 'Сохранение...' : (initialData ? 'Сохранить изменения' : 'Создать')}
      </button>
    </Modal>
  );
};
