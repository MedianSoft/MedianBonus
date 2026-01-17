import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'

// https://vite.dev/config/
export default defineConfig({
  server: {
    port: 3000,  // Specifies the port for the development server
    host: '0.0.0.0', // Expose to network
  },
  plugins: [
    react(),  // Enables React support in Vite
    tsconfigPaths(),  // Enables automatic TypeScript path mapping based on `tsconfig.json`
  ],
})
