import { createBrowserRouter } from 'react-router-dom'
import DashboardPage from '@/pages/dashboard/DashboardPage'
import LoginPage from '@/pages/auth/LoginPage'
import RegisterPage from "@/pages/auth/RegisterPage";

export const router = createBrowserRouter([
  { path: '/', element: <DashboardPage /> },
  { path: '/login', element: <LoginPage /> },
  { path: "/register", element: <RegisterPage /> },
])
