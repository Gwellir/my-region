import React from "react"

const Registred = () => {
    return (
        <div>
            <div className="flex justify-end cursor-pointer">
                <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M8.733 7.75208L14.0963 2.38882L12.682 0.974609L7.31879 6.33786L1.95554 0.974609L0.541322 2.38882L5.90457 7.75208L0.359375 13.2973L1.77359 14.7115L7.31879 9.16629L12.864 14.7115L14.2782 13.2973L8.733 7.75208Z" fill="black" />
                </svg>
            </div>
            <span className="flex justify-center font-jost font-bold text-registerText">Регистрация</span>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Организатор / Участник</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Имя и Фамилия</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Номер телефона</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Электронная почта</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Пароль</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <div className="flex flex-col pt-7 pb-3">
                <span className="font-jost text-titleRegister pb-1">Подтвердить пароль</span>
                <input className="px-6 h-14 rounded-3xl focus:outline-none"></input>
            </div>
            <button className="w-full font-jost text-registerText px-6 h-14 rounded-3xl bg-btmReg focus:outline-none">Зарегистрироваться</button>
        </div>
    )
}

export default Registred