import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { businessApi } from "@/shared/api/business";
import { useNotification } from "@/shared/lib/hooks/useNotification";

export default function RegisterPage() {
  const navigate = useNavigate();
  const notify = useNotification();

  // Состояния для полей формы
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await businessApi.create({ email, name, password });

      if (response.ok) {
        notify.showSuccess("Регистрация успешна!");
        navigate("/login");
      } else {
        notify.showError("Ошибка регистрации. Возможно, email занят.");
      }
    } catch (err) {
      notify.showError("Сервер недоступен");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleRegister} className="p-8 bg-white shadow-lg rounded-lg w-96">
        <h2 className="text-2xl font-bold mb-6 text-center">Регистрация</h2>

        <input
          type="text"
          placeholder="Имя"
          className="w-full p-2 mb-4 border rounded"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email"
          className="w-full p-2 mb-4 border rounded"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Пароль"
          className="w-full p-2 mb-6 border rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

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
