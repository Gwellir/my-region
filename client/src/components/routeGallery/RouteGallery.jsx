import React from 'react'

import teslaFoto from '../../images/route/tesla-foto.png'
import monastery from '../../images/route/monastery.png'
import istra from '../../images/route/istra.png'
import monument from '../../images/route/monument.png'
import monumentIl2 from '../../images/route/monument-il2.png'
import sculpture from '../../images/route/sculpture.png'

const RouteGallery = () => {
    return (
        <div className="flex flex-wrap justify-center pl-8 pt-20">
        <img className="w-32 h-32 p-1.5" src={teslaFoto} alt="teslaFoto" />
        <img className="w-32 h-32 p-1.5" src={monastery} alt="monastery" />
        <img className="w-32 h-32 p-1.5" src={istra} alt="istra" />
        <img className="w-32 h-32 p-1.5" src={monument} alt="monument" />
        <img className="w-32 h-32 p-1.5" src={monumentIl2} alt="monumentIl2" />
        <img className="w-32 h-32 p-1.5" src={sculpture} alt="sculpture" />
    </div>
    )
}

export default RouteGallery