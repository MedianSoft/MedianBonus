import { useState } from 'react';

export interface NotificationState {
  isOpen: boolean;
  type: 'success' | 'error';
  title: string;
  message: string;
}

export function useNotification() {
  const [notification, setNotification] = useState<NotificationState>({
    isOpen: false,
    type: 'success',
    title: '',
    message: ''
  });

  const showSuccess = (message: string = 'Операция выполнена успешно') => {
    setNotification({
      isOpen: true,
      type: 'success',
      title: 'Успешно!',
      message
    });
  };

  const showError = (message: string = 'Произошла непредвиденная ошибка') => {
    setNotification({
      isOpen: true,
      type: 'error',
      title: 'Ошибка',
      message
    });
  };

  const closeNotification = () => {
    setNotification(prev => ({ ...prev, isOpen: false }));
  };

  return { notification, showSuccess, showError, closeNotification };
}
