module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: (image) => ({
        "main-logo":
          "url('images/icons/MainLogo.png')",
      }),
      backgroundColor: (theme) => ({
        primary: "#ffffff",
        secondary: "#E7EEE7",
        bgBtn: "#2D6501"
      }),
      colors: {
        textBlack: "#1F1C45",
        textRegionColor: "#D9D9D9"
      },
      fontSize: {
        sm: ['12px', '14px'],
        logoSize: ['25px', '30px'],
        textSeach: ['20px', '20px'],
        textRegion: ['17px', '20px'],
        textCard: ['18px', '20px']
      },
      fontFamily: {
        sans: ['arkhip'],
        jost: ['jost']
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
