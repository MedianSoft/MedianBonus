import Header from '@/widgets/Header/Header';
import { useState } from 'react';

// Типизация для пользователя
interface User {
  id: number;
  name: string;
  email: string;
  bonusBalance: number;
}

export default function AdminDashboard() {
  // Фейковые данные для верстки (замените на fetch в будущем)
  const [users] = useState<User[]>([
    { id: 1, name: "Иван Иванов", email: "ivan@mail.com", bonusBalance: 1500 },
    { id: 2, name: "Мария Сидорова", email: "masha@test.ru", bonusBalance: 2300 },
  ]);

  return (
    <div className="min-h-screen bg-[#121212] text-white">
      <Header />

      <main className="p-6 max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">Панель администратора</h1>
          <button className="bg-orange-500 hover:bg-orange-600 px-4 py-2 rounded-lg transition-colors">
            + Добавить пользователя
          </button>
        </div>

        {/* Секция статистики системы */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-[#1e1e1e] p-6 rounded-2xl border border-gray-800">
            <p className="text-gray-400 text-sm">Всего пользователей</p>
            <p className="text-3xl font-bold">1,240</p>
          </div>
          <div className="bg-[#1e1e1e] p-6 rounded-2xl border border-gray-800">
            <p className="text-gray-400 text-sm">Выдано бонусов (всего)</p>
            <p className="text-3xl font-bold text-orange-500">450,000</p>
          </div>
          <div className="bg-[#1e1e1e] p-6 rounded-2xl border border-gray-800">
            <p className="text-gray-400 text-sm">Активные сегодня</p>
            <p className="text-3xl font-bold text-green-500">89</p>
          </div>
        </div>

        {/* Таблица управления пользователями */}
        <div className="bg-[#1e1e1e] rounded-2xl border border-gray-800 overflow-hidden">
          <table className="w-full text-left">
            <thead className="bg-[#252525] text-gray-400 uppercase text-xs uppercase">
              <tr>
                <th className="p-4">Имя</th>
                <th className="p-4">Email</th>
                <th className="p-4">Баланс</th>
                <th className="p-4 text-right">Действия</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-800">
              {users.map(user => (
                <tr key={user.id} className="hover:bg-[#252525] transition-colors">
                  <td className="p-4 font-medium">{user.name}</td>
                  <td className="p-4 text-gray-400">{user.email}</td>
                  <td className="p-4 text-orange-400">{user.bonusBalance} Б</td>
                  <td className="p-4 text-right">
                    <button className="text-blue-400 hover:underline mr-4">Изменить</button>
                    <button className="text-red-400 hover:underline">Удалить</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
