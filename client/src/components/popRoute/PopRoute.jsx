import React from "react"
import { Link } from "react-router-dom"

import Tesla from "../../images/route/tesla.png"
import star from  "../../images/icons/star.png"
import clock from  "../../images/icons/clock.png"
import LogoTrack from  "../../images/icons/LogoTrack.png"
import line from "../../images/icons/line.png"

const getStars = () => {
    let content = [];
    for (let i = 0; i < 5; i++) {
    content.push(<img key={i} className="p-0.5 w-5 h-5" src={star} alt="star"/>);
    }
    return content;
     };
const getRoute = () => {
  let content = [];
  for (let i = 0; i < 3; i++) {
    content.push(
      <div className="w-1/4 pl-8 mt-11 relative shadow-shadowRoute">
        <img className="w-72 h-56 pr-8 pt-9 pb-5 " src={Tesla} alt="Tesla" />
        <div className="flex absolute right-12 top-12">{getStars()}</div>
        <span className="flex font-bold text-textSeach font-jost pt-2.5 pb-1">
          Костромские красоты
        </span>
        <span className="flex font-jost text-textRegion text-textRegionColor">
          Костромская область
        </span>
        <p className="font-jost">Самый быстрый и удобный маршрут.</p>
        <div className="flex pt-3 pb-8">
          <img src={clock} alt="clock" />
          <span className="pl-3 text-textCard font-jost">1 день</span>
          <img className="px-5" src={line} alt="line" />
          <img src={LogoTrack} alt="logoTrack" />
          <span className="pl-3 text-textCard font-jost">Пеший</span>
        </div>
        <Link to="RoutePage">
          <button className=" mb-9 focus:outline-none bg-bgBtn w-72 h-11 rounded-3xl text-white font-jostmd text-base">
            Подробнее
          </button>
        </Link>
      </div>
    );
  }
  return content;
};

const PopRoute = () => {
    return (
      <div className="w-auto bg-primary pb-36">
        <span className="flex justify-center pt-20 font-jost font-bold text-xl pb-11">
          Популярные маршруты
        </span>
        <div className="flex justify-around">{getRoute()}</div>
        <div className="flex justify-around">{getRoute()}</div>
      </div>
    );
}

export default PopRoute