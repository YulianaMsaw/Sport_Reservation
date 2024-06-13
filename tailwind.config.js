/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#000000',
        secondary: '#f3f3f3'
      },
      fontFamily: {
        inter: ['Inter']
      }
    }
  },
  plugins: []
}
