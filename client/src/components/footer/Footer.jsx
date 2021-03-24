import React from "react"
import MainLogo from "../../images/icons/MainLogo.png"
import social from "../../images/icons/social.png"

const getSocial = () => {
    let content = [];
    for (let i = 0; i < 5; i++) {
    content.push(<img key={i} className="pl-6" src={social} alt="social"/>);
    }
    return content;
     };

const Footer = () => {
    return (
        <div className="w-auto bg-primary">
            <div className="flex justify-around pt-16 px-8 pb-11">
            <div className="flex flex-col">
                <div className="flex items-center pb-5">
                    <img className="h-16" src={MainLogo} alt="mainLogo" />
                    <span className="font-sans text-logoSize tracking-widest">мой край</span>
                </div>
                <span className="w-64 font-jost text-addressSize pb-1">г.Москва, ул.Родионова 13, офис 156</span>
                <span className="font-jost text-telSize">+7 (982) 234 45 28</span>
            </div>
            <div className="flex flex-col mt-3.5">
                <span className="font-jost text-addressSize font-medium pb-2">Ссылки</span>
                <span className="font-jost text-addressSize pb-2">Маршруты</span>
                <span className="font-jost text-addressSize pb-2">Обучение</span>
                <span className="font-jost text-addressSize pb-2">Личный кабинет</span>
            </div>
            <div className="flex flex-col mt-3.5">
                <span className="font-jost text-addressSize font-medium pb-2">Организациям</span>
                <span className="font-jost text-addressSize pb-2">ООПТ</span>
                <span className="font-jost text-addressSize pb-2">Тарифы</span>
                <span className="font-jost text-addressSize pb-2">Сотрудничество</span>
            </div>
            <div className="flex flex-col mt-3.5">
                <span className="font-jost text-addressSize font-medium pb-2">Обратная связь</span>
                <span className="font-jost text-addressSize pb-2">Вакансии</span>
                <span className="font-jost text-addressSize pb-2">Контакты</span>
                <span className="font-jost text-addressSize pb-2">Обратная связь</span>
            </div>
            </div>
            <div className="flex pb-44 justify-center">
               {getSocial()}
            </div>
        </div>
    )
}

export default Footer