import { Navigate, Outlet } from "react-router-dom";

export const ProtectedRoute = () => {
  const token = localStorage.getItem("access_token");

  // Если токена нет — отправляем на приветственный экран
  if (!token) {
    return <Navigate to="/welcome" replace />;
  }

  return <Outlet />;
};
