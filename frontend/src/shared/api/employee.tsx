import type { Employee, CreateEmployeeDto, GetAllEmployeesResponse } from '@/shared/types/employee';

const API_URL = `${__API_URL__}/employee`;

export const employeeApi = {
  create: (data: CreateEmployeeDto) =>
    fetch(`${API_URL}/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }),

  update: (data: Partial<Employee>) =>
    fetch(`${API_URL}/update`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }),

  delete: (id: string) =>
    fetch(`${API_URL}/delete`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id }),
    }),

  getById: (id: string): Promise<Employee> =>
    fetch(`${API_URL}/${id}`, {
      method: 'GET',
      headers: { 'accept': 'application/json' }
    }).then(r => r.json()),

  getAll: (): Promise<{ employees: Employee[] }> =>
    fetch(`${API_URL}/`, {
      method: 'GET',
      headers: { 'accept': 'application/json' }
    }).then(r => r.json()),

  getByEmail: (email: string): Promise<Employee> =>
    fetch(`${API_URL}/get_by_email`, {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email }),
    }).then(r => {
      if (!r.ok) throw new Error('Сотрудник не найден');
      return r.json();
    }),
};
