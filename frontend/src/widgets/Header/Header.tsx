import { useNavigate } from "react-router-dom";

export default function Header() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Очистка данных авторизации
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <header className="flex items-center justify-between px-6 py-4 bg-white border-b border-gray-200">
      <div className="flex items-center gap-2">
        <div className="w-8 h-8 bg-orange-500 rounded-lg"></div> {/* Заглушка логотипа */}
        <span className="text-xl font-bold text-gray-800">Median Bonus</span>
      </div>
      
      <div className="flex items-center gap-4">
        <nav className="hidden md:flex gap-6 mr-6">
          <a href="#" className="text-sm font-medium text-gray-600 hover:text-orange-500">Главная</a>
          <a href="#" className="text-sm font-medium text-gray-600 hover:text-orange-500">История</a>
        </nav>
        
        <button 
          onClick={handleLogout}
          className="px-4 py-2 text-sm font-medium text-red-600 border border-red-200 rounded-lg hover:bg-red-50"
        >
          Выйти
        </button>
      </div>
    </header>
  );
}
