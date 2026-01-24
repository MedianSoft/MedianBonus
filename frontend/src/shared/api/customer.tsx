import type { Customer, CreateCustomerDto, GetAllCustomersResponse } from '@/shared/types/customer';

const API_URL = `${__API_URL__}/customer`;

export const customerApi = {
  create: (data: CreateCustomerDto) =>
    fetch(`${API_URL}/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }),

  update: (data: Customer) =>
    fetch(`${API_URL}/update`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }),

  getById: (id: string) =>
    fetch(`${API_URL}/${id}`, {
      method: 'GET',
      headers: { 'accept': 'application/json' }
    }).then(r => {
      if (!r.ok) throw new Error('Клиент не найден');
      return r.json();
    }),

  getAll: (): Promise<Customer[]> =>
    fetch(`${API_URL}/`, {
      method: 'GET',
      headers: { 'accept': 'application/json' }
    }).then(r => r.json()),

  delete: (id: string) =>
    fetch(`${API_URL}/delete`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id }),
    }),

  getByPhone: (phone: string): Promise<Customer> =>
    fetch(`${__API_URL__}/customer/get_by_phone`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone }),
    }).then(r => {
      if (!r.ok) throw new Error('Клиент не найден');
      return r.json();
    }),
};
