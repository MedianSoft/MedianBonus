import { ReactNode } from 'react';
import Header from '@/widgets/Header/Header';
import { Sidebar } from '@/widgets/Sidebar/Sidebar';
import type { UserRole } from '@/shared/types/user';

interface AdminLayoutProps {
  children: ReactNode;
  activeTab: string;
  setActiveTab: (id: string) => void;
  role: UserRole;
  onQuickCreate: (id: string) => void;
}

export const AdminLayout = ({ children, activeTab, setActiveTab, role, onQuickCreate }: AdminLayoutProps) => {
  return (
    /* flex-col делает Header и нижний блок вертикальными */
    <div className="flex flex-col min-h-screen bg-app-bg]">

      {/* 1. Хедер всегда сверху на 100% ширины */}
      <Header />

      {/* 2. Контейнер для нижних блоков (Sidebar + Main) */}
      <div className="flex flex-1">
        <Sidebar
          activeTab={activeTab}
          onTabChange={setActiveTab}
          onQuickCreate={onQuickCreate}
          userRole={role}
        />

        {/* Контент справа от сайдбара */}
        <main className="flex-1 p-8 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  );
};
