module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      width: {
        '30': '30rem',
      },
      backgroundImage:{
        'hero-bg': "url('/Hero.svg')"
      }
    },
  },
  plugins: [],
}
