import { Modal } from '@/shared/ui/Modal/Modal';

export interface NotificationState {
  isOpen: boolean;
  type: 'success' | 'error';
  title: string;
  message: string;
}

interface Props {
  state: NotificationState;
  onClose: () => void;
}

export const NotificationModal = ({ state, onClose }: Props) => {
  return (
    <Modal isOpen={state.isOpen} onClose={onClose} title={state.title}>
      <div className="flex flex-col items-center text-center space-y-4 py-4">
        <div className={`w-16 h-16 rounded-full flex items-center justify-center text-3xl ${
          state.type === 'success' ? 'bg-green-500/20 text-green-500' : 'bg-red-500/20 text-red-500'
        }`}>
          {state.type === 'success' ? '✓' : '✕'}
        </div>
        <p className="text-gray-300">{state.message}</p>
        <button
          onClick={onClose}
          className="w-full bg-gray-800 hover:bg-gray-700 text-white py-3 rounded-xl transition-colors mt-4"
        >
          Понятно
        </button>
      </div>
    </Modal>
  );
};
