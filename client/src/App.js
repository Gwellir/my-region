import React from "react"
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Header from "./components/header/Header"
import Footer from "./components/footer/Footer"

import MainPage from "./page/MainPage"
import UserPage from "./page/UserPage"
import RoutePage from "./page/RoutePage"
import ScrollToTop from "./components/ScrollToTop"

function App() {

  return (
    <React.StrictMode>
        <Router>
        <ScrollToTop />
        <Header />
          <Switch>
            <Route exact path="/" component={MainPage} />
            <Route path='/UserPage' component={UserPage} />
            <Route path='/RoutePage' component={RoutePage} />
          </Switch>
          <Footer /> 
        </Router>
      </React.StrictMode>
  )
}

export default App
