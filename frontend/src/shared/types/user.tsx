export type UserRole = 'admin' | 'manager' | 'employee';

export interface User {
  id: string;
  name: string;
  email: string;
  status: 'activated' | 'deactivated';
  role: UserRole;
}
