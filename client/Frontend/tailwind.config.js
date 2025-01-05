/** @type {import('tailwindcss').Config} */

const colors = {
  primary: "#ef495d",
};

export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: colors,
      fontFamily: {
        workSans: ["workSans", "sans-serif"],
      },
    },
  },
  plugins: [],
};
