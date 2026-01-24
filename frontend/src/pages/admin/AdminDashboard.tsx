import { useState } from 'react';
import { AdminLayout } from '@/widgets/AdminLayout/ui/AdminLayout';
import { EmployeeManagement } from '@/widgets/EmployeeManagement/ui/EmployeeManagement';
import { useEmployees } from '@/widgets/EmployeeManagement/model/useEmployees';
import { CustomerManagement } from '@/widgets/CustomerManagement/ui/CustomerManagement';
import { useCustomers } from '@/widgets/CustomerManagement/model/useCustomers';
import { StatsCard } from '@/shared/ui/StatsCard/StatsCard';
import type { UserRole } from '@/shared/types/user';

export default function AdminDashboard() {
  const [activeTab, setActiveTab] = useState('stats');
  const [role] = useState<UserRole>('admin');
  const employeeController = useEmployees();
  const customerController = useCustomers();

  // Логика быстрого создания
  const handleQuickCreate = (tabId: string) => {
    setActiveTab(tabId);
    // Если кликаем + на пользователях или сотрудниках — открываем модалку
    if (tabId === 'stats' || tabId === 'employees') {
      employeeController.setIsModalOpen(true);
    }
  };
  return (
    <AdminLayout
      activeTab={activeTab}
      setActiveTab={setActiveTab}
      role={role}
      onQuickCreate={handleQuickCreate}
    >
      {activeTab === 'stats' && (
        <section className="animate-in fade-in duration-500">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <StatsCard title="Всего пользователей" value="1,240" />
            <StatsCard title="Выдано бонусов" value="450,000" color="orange" />
            <StatsCard title="Активные сегодня" value="89" color="green" />
          </div>
           <CustomerManagement
            controller={customerController}
            title="Управление клиентами"
          />
        </section>
      )}

      {activeTab === 'shops' && (
        <div className="bg-app-surface p-10 rounded-2xl border border-dashed border-gray-800 text-center
        italic">
          Модуль управления магазинами находится в разработке...
        </div>
      )}

      {activeTab === 'employees' && (
        <div className="animate-in slide-in-from-bottom-2 duration-400">
           <EmployeeManagement
            controller={employeeController}
            title="Управление сотрудниками"
          />
        </div>
      )}
    </AdminLayout>
  );
}
