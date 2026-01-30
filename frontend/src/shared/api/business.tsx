const API_URL = `${__API_URL__}/business`;

export const businessApi = {
  create: (data: any) =>
    fetch(`${API_URL}/create`, {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    }),
};
