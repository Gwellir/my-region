import React from 'react'
import Header from "../components/header/Header"
import Search from "../components/search/Search"
import Map from "../components/map/Map"
import PopRoute from "../components/popRoute/PopRoute"
import Reviews from "../components/reviews/Reviews"
import Footer from "../components/footer/Footer"

const MainPage = () => {
    return (
        <div className="flex flex-col justify-items-center">
            <Header />
            <Search />
            <Map />
            <PopRoute />
            <Reviews />
            <Footer />
        </div>
    )
}

export default MainPage