import { useNavigate, Link } from "react-router-dom";

export default function RegisterPage() {
  const navigate = useNavigate();

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    // Логика регистрации...
    navigate("/login");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleRegister} className="p-8 bg-white shadow-lg rounded-lg w-96">
        <h2 className="text-2xl font-bold mb-6 text-center">Регистрация</h2>
        <input type="text" placeholder="Имя" className="w-full p-2 mb-4 border rounded" required />
        <input type="email" placeholder="Email" className="w-full p-2 mb-4 border rounded" required />
        <input type="password" placeholder="Пароль" className="w-full p-2 mb-6 border rounded" required />
        <button type="submit" className="w-full bg-green-600 text-white p-2 rounded hover:bg-green-700">
          Создать аккаунт
        </button>
        <p className="mt-4 text-sm text-center">
          Уже есть аккаунт? <Link to="/login" className="text-blue-600">Войти</Link>
        </p>
      </form>
    </div>
  );
}
