import React, { createContext, useContext, useState, useCallback } from 'react';
import { NotificationModal } from '@/shared/ui/NotificationModal/NotificationModal';
import type { NotificationState } from '@/shared/ui/NotificationModal/NotificationModal';

interface NotificationContextType {
  showSuccess: (msg: string, title?: string) => void;
  showError: (msg: string, title?: string) => void;
}

const NotificationContext = createContext<NotificationContextType | null>(null);

export const NotificationProvider = ({ children }: { children: React.ReactNode }) => {
  const [state, setState] = useState<NotificationState>({
    isOpen: false,
    type: 'success',
    title: '',
    message: ''
  });

  const showSuccess = useCallback((msg: string, title: string = 'Успешно') => {
    setState({
      isOpen: true,
      type: 'success',
      title,
      message: msg
    });
  }, []);

  const showError = useCallback((msg: string, title: string = 'Ошибка') => {
    setState({
      isOpen: true,
      type: 'error',
      title,
      message: msg
    });
  }, []);

  const handleClose = () => setState(prev => ({ ...prev, isOpen: false }));

  return (
    <NotificationContext.Provider value={{ showSuccess, showError }}>
      {children}
      <NotificationModal
        state={state}
        onClose={handleClose}
      />
    </NotificationContext.Provider>
  );
};

export const useNotification = () => {
  const context = useContext(NotificationContext);
  if (!context) throw new Error("useNotification must be used within NotificationProvider");
  return context;
};
