import React from 'react'

import avatar from '../../images/route/avatar.png'
import star from '../../images/icons/star.png'

const getStars = (k) => {
    let content = [];
    for (let i = 0; i < k; i++) {
        content.push(<img key={i} className="p-0.5 w-5 h-5" src={star} alt="star" />);
    }
    return content;
};

const RouteInfoAuthor = () => {
    return (
        <div className="flex items-center rounded-md bg-bgInfo mt-3">
            <img className="p-6" src={avatar} alt="avatar" />
            <div className="flex flex-col">
                <span className="font-jost text-textGreyAuthor text-authorSize">Автор маршрута</span>
                <span className="font-jostmd text-titleRegister">Юлия Жукова</span>
                <div className="flex">{getStars(4)}</div>
                <button className="rounded-3xl bg-btmReg text-white mt-2 text-detailSize w-32 h-7">Подробнее</button>
            </div>
        </div>
    )
}

export default RouteInfoAuthor