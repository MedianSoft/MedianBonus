import { useNavigate, Link } from "react-router-dom";

export default function LoginPage() {
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Здесь будет логика запроса к API
    localStorage.setItem("token", "fake-jwt-token"); // Имитация входа
    navigate("/");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleSubmit} className="p-8 bg-white shadow-lg rounded-lg w-96">
        <h2 className="text-2xl font-bold mb-6 text-center">Вход</h2>
        <input type="email" placeholder="Email" className="w-full p-2 mb-4 border rounded" required />
        <input type="password" placeholder="Пароль" className="w-full p-2 mb-6 border rounded" required />
        <button type="submit" className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700">
          Войти
        </button>
        <p className="mt-4 text-sm text-center">
          Нет аккаунта? <Link hide-focus="true" to="/register" className="text-blue-600">Регистрация</Link>
        </p>
      </form>
    </div>
  );
}
