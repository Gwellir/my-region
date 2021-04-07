module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    boxShadow: {
      shadowRoute: "0px 1px 9px 0px rgba(44, 84, 13, 0.2)",
    },
    borderColor: theme => ({
      'btnGreen': '#477D1C',
      'tableGrey': '#D2D2D2'
     }),
    extend: {
      backgroundColor: (theme) => ({
        primary: "#ffffff",
        secondary: "#E7EEE7",
        bgBtn: "#2D6501",
        btmReg: "#9BACA0",
        btnBlock: "#477D1C",
        bgInfo: "#ECF0F4",
      }),
      outline: {
        green: '2px solid #477D1C',
      },
      colors: {
        textBlack: "#1F1C45",
        textRegionColor: "#767676",
        dateReviewes: "#BEBEBE",
        hoverSearch: "#477D1C",
        textGrey: "#ABABAB",
        textGreyAuthor: "#A9A9A9"
      },
      fontSize: {
        sm: ['12px', '14px'],
        logoSize: ['25px', '30px'],
        textSeach: ['20px', '20px'],
        textRegion: ['17px', '20px'],
        textCard: ['18px', '20px'],
        titleReviews: ['22px', '20px'],
        dateReviewesSize: ['19px', '20px'],
        pReviews: ['20px', '21px'],
        addressSize:['20px', '29px'],
        telSize: ['19px', '27px'],
        registerText: ['24px', '35px'],
        titleRegister: ['18px', '26px'],
        detailSize: ['14px', '20px'],
        authorSize: ['16px', '23px'],
        tourTitle: ['24px', '20px'],
        tourCar: ['22px', '32px']
      },
      fontFamily: {
        sans: ['arkhip'],
        jost: ['jost'],
        jostmd: ['jostmd'],
        jostBold: ['jostBold']
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
