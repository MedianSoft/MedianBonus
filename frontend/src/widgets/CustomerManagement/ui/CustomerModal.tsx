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
  // Валидация полей
  const isNameMinOk = form.name.trim().length >= 2;
  const isNameMaxOk = form.name.length <= 50;
  const isNameValid = isNameMinOk && isNameMaxOk;
  // Валидация телефона (только цифры)
  const phoneDigits = form.phone.replace(/\D/g, '');
  const isPhoneLengthOk = phoneDigits.length >= 10 && phoneDigits.length <= 15;

  const isFormInvalid = !isNameValid || !isPhoneLengthOk;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={initialData ? "Изменить клиента" : "Новый клиент"}>
      <div className="space-y-5">
        <div className="flex flex-col gap-1.5">
          <label className="text-xs font-semibold text-gray-500 uppercase">Имя клиента</label>
          <input
            maxLength={51}
            className={`w-full bg-[#252525] border ${form.name.length > 50 ? 'border-red-500' : 'border-gray-700'} p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-all`}
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
          />
          {form.name.length > 0 && !isNameMinOk && (
            <p className="text-red-500 text-xs mt-1 ml-1 animate-in fade-in duration-300">Минимум 2 символа</p>
          )}
          {form.name.length > 50 && (
            <p className="text-red-500 text-xs mt-1 ml-1 animate-in fade-in duration-300">Максимум 50 символов</p>
          )}
        </div>
        <div className="flex flex-col gap-1.5">
          <label className="text-xs font-semibold text-gray-500 uppercase">Телефон</label>
          <input
            className={`w-full bg-[#252525] border ${form.phone.length > 0 && !isPhoneLengthOk ? 'border-red-500' : 'border-gray-700'} p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-all`}
            placeholder="+79000000000"
            value={form.phone}
            onChange={e => setForm({...form, phone: e.target.value})}
          />
          {form.phone.length > 0 && !isPhoneLengthOk && (
            <p className="text-red-500 text-xs mt-1 ml-1 animate-in fade-in duration-300">Введите минимум 10 цифр номера</p>
          )}
        </div>
      </div>
      <button
        onClick={() => onSave(form)}
        disabled={loading || isFormInvalid}
        className={`w-full bg-orange-500 mt-8 py-3 rounded-xl text-white font-bold transition-all ${
          (loading || isFormInvalid) ? 'opacity-20 cursor-not-allowed' : 'hover:bg-orange-600 active:scale-[0.98]'
        }`}
      >
        {loading ? 'Сохранение...' : (initialData ? 'Сохранить изменения' : 'Создать')}
      </button>
    </Modal>
  );
};
