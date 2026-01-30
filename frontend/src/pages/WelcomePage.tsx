import { Link } from "react-router-dom";

export default function WelcomePage() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50">
      <h1 className="text-4xl font-bold mb-4 text-gray-800">Median Bonus</h1>
      <p className="text-gray-600 mb-8">Система лояльности для вашего бизнеса</p>
      <div className="flex gap-4">
        <Link to="/login" className="bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition">
          Войти
        </Link>
        <Link to="/register" className="bg-green-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition">
          Стать партнером
        </Link>
      </div>
    </div>
  );
}