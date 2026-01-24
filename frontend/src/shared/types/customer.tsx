export interface Customer {
  id: string;
  name: string;
  phone: string;
}

export interface CreateCustomerDto {
  name: string;
  phone: string;
}

export interface GetAllCustomersResponse {
  customers: Customer[];
}
