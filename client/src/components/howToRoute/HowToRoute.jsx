import React from 'react'

const HowToRoute = () => {
    return (
        <div className="flex flex-col w-3/4 pl-20">
            <span className="font-jostmd text-registerText text-hoverSearch pb-3">Как добраться:</span>
            <span className="font-jostmd text-tourCar p-0.5">На личном транспорте:</span>
            <p className="text-tourCar">
                Проложить маршрут до места сбора станция «Новоиерусалимская» Рижского направления»
                Координаты 55.912725, 36.823120
            </p>
            <span className="font-jostmd text-tourCar pt-5">На общественном транспорте:</span>
            <p className="text-tourCar pt-0.5">
                Электричка от ж/д станция  Тушинская (Тушино)
                до станции Новоиерусалимская» Рижского направления
            </p>
            <span className="font-jostmd text-tourCar pt-4">Достопримечательности:</span>
            <div className="flex flex-col">
                <span className="text-tourCar pt-0.5">Истринское водохранилище</span>
                <span className="text-tourCar pt-0.5">Башни Тесла</span>
                <span className="text-tourCar pt-0.5">Выставка старых автомобилей 1940-70-х годов</span>
                <span className="text-tourCar pt-0.5">Церковь Казанской иконы Божией Матери</span>
                <span className="text-tourCar pt-0.5">Воскресенский Ново-Иерусалимский ставропигиальный мужской монастырь</span>
                <span className="text-tourCar pt-0.5">Скит патриарха Никона </span>
                <span className="text-tourCar pt-0.5">Памятники А.Чехов и И.Левитан</span>
                <span className="text-tourCar pt-0.5">Памятник Леонардо да Винчи</span>
                <span className="text-tourCar pt-0.5">Памятник Дама с собачкой</span>
            </div>
        </div>
    )
}

export default HowToRoute