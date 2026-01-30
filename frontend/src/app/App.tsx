import { RouterProvider } from 'react-router-dom'
import { router } from './router'
import { NotificationProvider } from '@/shared/lib/providers/NotificationProvider';

export default function App() {
  return (
    <NotificationProvider>
      <RouterProvider router={router} />
    </NotificationProvider>
  );
}
