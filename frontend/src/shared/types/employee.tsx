export interface Employees {
  id: string;
  name: string;
  email: string;
  status: 'activated' | 'deactivated';
}

export interface GetAllEmployeesResponse {
  employees: Employee[];
}

export interface CreateEmployeeDto {
  name: string;
  email: string;
  password?: string;
  business_id: string;
}
