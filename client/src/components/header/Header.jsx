import React, { useState } from "react"
import { Link } from "react-router-dom"
import ModalMain from "../../components/modalMain/ModalMain"
import MainLogo from "../../images/icons/MainLogo.png"
import Registred from "../../components/registred/registred"
import Login from "../../components/login/login"
import line from "../../images/icons/line.png"


const Header = () => {
  const [modalActive, setModalActive] = useState(false)
  const [logAct, setLogAct] = useState(false)
  return (
    <header className="flex items-center justify-around w-auto h-28 bg-primary">
      <Link to="/">
        <div className="flex items-center px-2 cursor-pointer">
          <img src={MainLogo} className="h-20 " alt="mainLogo" />
          <div className="flex flex-col">
            <span className="text-textBlack text-logoSize font-sans py-1 tracking-widest">
              мой край
            </span>
            <span className="text-textBlack font-sans font-normal text-sm">
              Сервис путешествий по России
            </span>
          </div>
        </div>
      </Link>
      <div className="flex-row justify-center w-1/3">
      <Link to="/">
        <span className="px-6 text-textSeach font-jost text-black hover:text-gray-400 cursor-pointer">Главная</span>
      </Link>
        <span className="px-6 text-textSeach font-jost text-gray-400 hover:text-black cursor-pointer">Расписание</span>
        <span className="px-6 text-textSeach font-jost text-gray-400 hover:text-black cursor-pointer">Путешествинникам</span>
      </div>
      <div className="flex">
      <button className="px-5 text-textSeach text-gray-400 font-jost focus:outline-none hover:text-black" onClick={setLogAct}>Войти</button>
      <img className="" src={line} alt="line" />
        <button className="px-5 text-textSeach text-gray-400 font-jost focus:outline-none hover:text-black" onClick={setModalActive}>Регистрация</button>
      </div>
      <ModalMain active={modalActive} setActive={setModalActive} children={<Registred />}/>
      <ModalMain active={logAct} setActive={setLogAct} children={<Login />}/>
    </header>
  );
};

export default Header
