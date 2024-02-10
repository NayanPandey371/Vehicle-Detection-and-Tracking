/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,jsx}"],
  theme: {
    extend: {
      boxShadow: {
        'boxshadowcolor': 'rgba(215, 213, 213, 0.25) 0px 54px 55px, rgba(200, 199, 199, 0.12) 0px -12px 30px, rgba(212, 210, 210, 0.12) 0px 4px 6px, rgba(235, 233, 233, 0.17) 0px 12px 13px, rgba(230, 224, 224, 0.09) 0px -3px 5px'
      },
      colors: {
        "primary": "#7734e7"
      }
    },

  },
  plugins: [],
}