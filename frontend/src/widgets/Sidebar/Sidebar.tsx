import styles from './Sidebar.module.css'
import { Plus } from 'lucide-react'; // используй любые иконки

interface MenuItem {
  id: string;
  label: string;
  role?: UserRole[]; // для будущего ограничения прав
}

interface Props {
  activeTab: string;
  onTabChange: (id: string) => void;
  onQuickCreate: (id: string) => void;
  userRole: UserRole;
}

const MENU_ITEMS: MenuItem[] = [
  { id: 'stats', label: 'Статистика и пользователи' },
  { id: 'shops', label: 'Магазины' },
  { id: 'employees', label: 'Сотрудники' },
];

export const Sidebar = ({ activeTab, onTabChange, onQuickCreate, userRole }: Props) => {
  return (
    <aside className={styles.aside}>
      {/*}<div className="font-bold text-orange-500 text-xl border-b border-gray-800">*/}
      <div className={styles.asideHeader}>
        MEDIAN ADMIN
      </div>
      <nav className="flex-1 p-4 space-y-2">
        {MENU_ITEMS.map((item) => (
          <div key={item.id} className="group flex items-center justify-between">
            <button
              onClick={() => onTabChange(item.id)}
              className={`flex-1 text-left px-4 py-2 rounded-lg transition-colors ${
                activeTab === item.id ? 'bg-orange-500' : 'text-gray-400 hover:bg-gray-800'
              }`}
            >
              {item.label}
            </button>
            <button
              onClick={(e) => { e.stopPropagation(); onQuickCreate(item.id); }}
              className="opacity-0 group-hover:opacity-100 p-2 hover:text-orange-500 text-gray-500 transition-all"
            >
              <Plus size={18} />
            </button>
          </div>
        ))}
      </nav>
    </aside>
  );
};
