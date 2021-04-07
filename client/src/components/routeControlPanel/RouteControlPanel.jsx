import React from 'react'

const RouteControlPanel = () => {
    return (
        <div className="flex">
            <div>
                <button className="text-white bg-btnBlock font-jostmd focus:outline-none text-titleRegister w-44 h-12 rounded-md">Забронировать</button>
            </div>
            <div className="pl-2">
                <button className="font-jostmd text-titleRegister w-44 h-12 focus:outline-none border-2 border-btnGreen rounded-md">Скачать GPX-трек</button>
            </div>
        </div>
    )
}

export default RouteControlPanel