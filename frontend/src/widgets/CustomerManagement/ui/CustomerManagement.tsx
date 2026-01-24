import { useState } from 'react';
import { CustomerModal } from './CustomerModal';

interface Props {
  title: string;
  controller: any; // Твой хук useCustomers
}

export const CustomerManagement = ({ title, controller }: Props) => {
  const {
    customers,
    isModalOpen,
    openCreateModal,
     closeModal,
    setIsModalOpen,
    isLoading,
    handleSave,
    openEditModal,
    currentCustomer,
    findByPhone // Новая ручка поиска
  } = controller;

  const [phoneSearch, setPhoneSearch] = useState('');

  return (
    <section className="w-full">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <h2 className="text-2xl font-bold">{title}</h2>

        <div className="flex w-full md:w-auto gap-3">
          {/* Поиск по телефону */}
          <div className="flex bg-app-surface border border-gray-800 rounded-xl overflow-hidden focus-within:border-orange-500 transition-colors">
            <input
              type="text"
              placeholder="Поиск по телефону..."
              className="bg-transparent px-4 py-2 outline-none w-48"
              value={phoneSearch}
              onChange={(e) => setPhoneSearch(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && findByPhone(phoneSearch)}
            />
            <button
              onClick={() => findByPhone(phoneSearch)}
              className="px-4 bg-gray-800 text-gray-400 hover:text-orange-500 transition-colors"
            >
              Найти
            </button>
          </div>

          <button
            onClick={openCreateModal}
            className="bg-orange-500 hover:bg-orange-600 px-5 py-2 rounded-xl font-medium transition-all shadow-lg shadow-orange-500/10"
          >
            + Добавить пользователя
          </button>
        </div>
      </div>

      <div className="bg-app-surface rounded-2xl border border-gray-800 overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead className="bg-header-bg text-[11px] uppercase tracking-wider">
            <tr>
              <th className="p-4 font-semibold">Имя клиента</th>
              <th className="p-4 font-semibold">Телефон</th>
              <th className="p-4 font-semibold text-right">Действия</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {customers.length > 0 ? (
              customers.map((user: any) => (
                <tr key={user.id} className="hover:bg-[#252525]/50 transition-colors text-gray-200">
                  <td className="p-4 font-medium">{user.name}</td>
                  <td className="p-4 text-gray-400 font-mono">{user.phone}</td>
                  <td className="p-4 text-right">
                    <button
                      onClick={() => openEditModal(user)}
                      className="text-orange-500 hover:text-orange-400 text-sm mr-4"
                    >
                      Изменить
                    </button>
                    <button className="text-red-500/60 hover:text-red-500 text-sm">
                      Удалить
                    </button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={3} className="p-10 text-center text-gray-600">Клиенты не найдены</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      <CustomerModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSave={handleSave}
        loading={isLoading}
        initialData={currentCustomer}
      />
    </section>
  );
};
