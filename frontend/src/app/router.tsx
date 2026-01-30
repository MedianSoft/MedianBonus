import { createBrowserRouter, Navigate } from 'react-router-dom';
import AdminDashboard from '@/pages/admin/AdminDashboard';
import LoginPage from '@/pages/auth/LoginPage';
import RegisterPage from '@/pages/auth/RegisterPage';
import WelcomePage from '@/pages/WelcomePage';
import { ProtectedRoute } from '@/app/ProtectedRoute';

export const router = createBrowserRouter([
  // Доступно всем
  { path: "/welcome", element: <WelcomePage /> },
  { path: "/login", element: <LoginPage /> },
  { path: "/register", element: <RegisterPage /> },

  // Доступно только авторизованным
  {
    element: <ProtectedRoute />,
    children: [
      { path: "/", element: <AdminDashboard /> },
    ]
  },
  {
    element: <ProtectedRoute />,
    children: [
      { path: "/", element: <AdminDashboard /> },
    ]
  },

  // 3. Редирект по умолчанию
  // Если залогинен — ProtectedRoute отправит на "/", если нет — на "/welcome"
  { path: "*", element: <Navigate to="/" replace /> }
]);
