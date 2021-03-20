import React from "react"
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import MainPage from "./page/MainPage"
import UserPage from "./page/UserPage"
import RoutePage from "./page/RoutePage"

function App() {

  return (
    <React.StrictMode>
        <Router>
          <Switch>
            <Route exact path="/" component={MainPage} />
            <Route path='/UserPage' component={UserPage} />
            <Route path='/RoutePage' component={RoutePage} />
          </Switch>
        </Router>
      </React.StrictMode>
  )
}

export default App
