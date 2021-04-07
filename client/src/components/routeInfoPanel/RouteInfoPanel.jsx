import React from "react"

import RouteControlPanel from '../routeControlPanel/RouteControlPanel'
import RouteDetailInfo from '../routeDetailInfo/RouteDetailInfo'
import RouteInfoAutor from '../routeInfoAuthor/RouteInfoAuthor'
import RouteGallery from '../routeGallery/RouteGallery'



const RouteInfoPanel = () => {
    return (
        <div className="flex flex-col w-1/3">
            <div className="pl-24">
                <RouteControlPanel />
                <div className="pt-2.5">
                    <RouteDetailInfo />
                    <RouteInfoAutor />
                </div>
            </div>
            <RouteGallery />
        </div>
    )
}

export default RouteInfoPanel