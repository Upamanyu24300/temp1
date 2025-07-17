import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],

  server: {
    host: '0.0.0.0',
    port: 3000
  },
  define: {
    // Replace with your Railway backend URL after deployment
    __API_URL__: JSON.stringify(process.env.VITE_API_URL || 'http://localhost:8000')
  }
})
