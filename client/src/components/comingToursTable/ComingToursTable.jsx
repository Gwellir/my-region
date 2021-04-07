import React from 'react'

const getTable = () => {
    let content = [];
    for (let i = 0; i < 3; i++) {
        content.push(
        <tr>
            <td className="flex flex-col text-textCard border border-tableGrey text-center py-5"><span>06.04.2021</span><span>08.04.2021</span></td>
            <td className="text-textSeach border border-tableGrey text-center">Дарья Бойцова</td>
            <td className="text-textSeach border border-tableGrey text-center">Осталось 4 места</td>
            <td className="text-textSeach border border-tableGrey text-center">1490 р</td>
            <td className="text-textSeach border border-tableGrey text-center">
                <button className="text-white bg-btnBlock font-jostmd focus:outline-none text-titleRegister w-44 h-12 rounded-md">
                    Хочу в поход!
                </button>
            </td>
        </tr>
        );
    }
    return content;
};

const comingToursTable = () => {
    return (
        <div className="flex flex-col py-20 px-20">
            <span className="text-center font-jostBold text-tourTitle text-hoverSearch pb-11">БЛИЖАЙШИЕ АКТИВНЫЕ ТУРЫ</span>
            <table className="table-auto">
                <thead>
                    <tr>
                        <th className="w-1/6 font-jostmd text-addressSize border border-tableGrey py-7">Даты</th>
                        <th className="w-1/5 font-jostmd text-addressSize border border-tableGrey">Инструктор</th>
                        <th className="w-1/4 font-jostmd text-addressSize border border-tableGrey">Количество мест</th>
                        <th className="font-jostmd text-addressSize border border-tableGrey">Цена</th>
                        <th className="w-1/5 font-jostmd text-addressSize border border-tableGrey">Заявка</th>
                    </tr>
                </thead>
                <tbody>
                    {getTable()}
                </tbody>
            </table>
        </div>
    )
}

export default comingToursTable