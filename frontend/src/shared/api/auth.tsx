const API_URL = `${__API_URL__}/auth`;

export const authApi = {
  login: (data: any) =>
    fetch(`${API_URL}/login`, {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    }).then(async (r) => {
    if (!r.ok) {
      const errorData = await r.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Ошибка авторизации');
    }
    return r.json();
  }),

  refreshToken: () =>
    fetch(`${API_URL}/refresh_token`, {
      method: 'POST',
      headers: { 'accept': 'application/json' },
    }).then(r => r.json()),
};
