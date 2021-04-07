import React from 'react'
import Search from "../components/search/Search"
import Map from "../components/map/Map"
import PopRoute from "../components/popRoute/PopRoute"
import Reviews from "../components/reviews/Reviews"

const MainPage = () => {
    return (
        <div className="flex flex-col justify-items-center">
            <Search />
            <Map />
            <PopRoute />
            <Reviews />
        </div>
    )
}

export default MainPage