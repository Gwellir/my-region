import React from 'react'
import routeImage from '../../images/route/route.png'

const RouteContent = () => {
    return (
        <div className="flex pl-20 flex-col w-3/5">
            <img src={routeImage} alt="routeImage" />
            <span className="text-hoverSearch font-jostmd pt-11 text-registerText">Описание</span>
            <p className="text-addressSize pt-1.5">
                Наш маршрут начинается на станции Новоиерусалимская Рижского направления.
                Собравшись дружной компанией мы сразу отправимся в самое таинственное место маршрута - к башням Тесла, спустимся по горнолыжному склону с видом на Новоиерусалимский монастырь и, пробравшись через лес, отправимся к Истринскому водохранилищу.
                Дорога будет проходить вдоль реки Истра, на пути нам встретится памятник Левитану и Чехову, Истринская ГЭС, весь путь будет картинным и красочным. Приехав на водохранилище, мы разобьем лагерь в уютном месте.
            </p>
        </div>
    )
}

export default RouteContent