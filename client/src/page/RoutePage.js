import React from 'react'

import RouteTitle from '../components/routeTitle/RouteTitle'
import RouteContent from '../components/routeContent/RouteContent'
import RouteInfoPanel from '../components/routeInfoPanel/RouteInfoPanel'
import ComingToursTable from '../components/comingToursTable/ComingToursTable'
import HowToRoute from '../components/howToRoute/HowToRoute'

const RoutePage = () => {
    return (
        <div>
            <RouteTitle />
            <div className="flex">
                <RouteContent />
                <RouteInfoPanel />
            </div>
            <ComingToursTable />
            <HowToRoute />
        </div>
    )
}

export default RoutePage