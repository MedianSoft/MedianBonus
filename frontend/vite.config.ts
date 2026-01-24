import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'
import path from 'path'

export default defineConfig(({ mode }) => {
  // Пытаемся найти .env сначала в корне фронта, потом уровнем выше
  const env = loadEnv(mode, process.cwd(), '');
  const rootEnv = loadEnv(mode, path.resolve(__dirname, '../'), '');

  // Объединяем их (системные переменные Docker имеют приоритет)
  const BE_HOST = process.env.BE_HOST || env.BE_HOST || rootEnv.BE_HOST || 'localhost';
  const BE_PORT = process.env.BE_PORT_EXTERNAL || env.BE_PORT_EXTERNAL || '8000';

  const apiHost = BE_HOST === '0.0.0.0' ? 'localhost' : BE_HOST;
  const apiUrl = `http://${apiHost}:${BE_PORT}`;

  return {
    server: {
      // Берем порт из .env (FE_PORT), если нет - ставим 3000
      port: Number(env.FE_PORT) || 3000,
      host: '0.0.0.0', // Оставляем так, чтобы Docker мог прокинуть порты
    },
    plugins: [
      react(),
      tsconfigPaths(), // Твой плагин для @ алиасов
    ],
    define: {
      // Создаем глобальную переменную с адресом API для использования в коде
      __API_URL__: JSON.stringify(apiUrl),
    },
  }
})
