import { useState } from 'react';
import Header from '@/widgets/Header/Header';
import { Sidebar } from '@/widgets/Sidebar/Sidebar';
import { EmployeeManagement } from '@/widgets/EmployeeManagement/ui/EmployeeManagement';
import type { UserRole } from '@/shared/types/user';

export default function AdminDashboard() {
  const [activeTab, setActiveTab] = useState('stats');
  // В будущем роль будет приходить из контекста авторизации
  const [role] = useState<UserRole>('admin');

  const renderContent = () => {
    switch (activeTab) {
      case 'stats':
        return (
          <>
            {/* Твоя секция статистики из шаблона */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
               <StatsCard title="Всего пользователей" value="1,240" />
               <StatsCard title="Выдано бонусов" value="450,000" color="orange" />
               <StatsCard title="Активные сегодня" value="89" color="green" />
            </div>
            <EmployeeManagement title="Список пользователей" />
          </>
        );
      case 'shops':
        return <div className="text-white">Виджет управления магазинами (в разработке)</div>;
      case 'employees':
        return <EmployeeManagement title="Управление сотрудниками" />;
      default:
        return null;
    }
  };

  const handleQuickCreate = (tabId: string) => {
    setActiveTab(tabId);
    // Здесь можно через реф или стейт сразу открывать модалку в EmployeeManagement
    console.log(`Быстрое создание для: ${tabId}`);
  };

  return (
    <div className="flex min-h-screen bg-[#121212]">
      <Sidebar
        activeTab={activeTab}
        onTabChange={setActiveTab}
        onQuickCreate={handleQuickCreate}
        userRole={role}
      />

      <div className="flex-1 flex flex-col">
        <Header />
        <main className="p-8">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}

// Маленький вспомогательный компонент для чистоты кода
const StatsCard = ({ title, value, color }: any) => (
  <div className="bg-[#1E1E1E] p-6 rounded-2xl border border-gray-800">
    <p className="text-gray-400 text-sm">{title}</p>
    <p className={`text-3xl font-bold ${color === 'orange' ? 'text-orange-500' : color === 'green' ? 'text-green-500' : 'text-white'}`}>
      {value}
    </p>
  </div>
);
