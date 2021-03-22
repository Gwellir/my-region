import React from "react"

const Search = () => {
  return (
    <div className="flex-none w-auto h-64 bg-secondary">
      <span className="flex justify-center font-jost font-bold uppercase pt-20 pb-10">
        Подобрать поход или активный тур
      </span>
      <div className="flex justify-center h-60px">
        <button className="bg-white py-3 px-7 inline-flex items-center rounded-l-lg focus:outline-none">
          <span className="pr-4 font-jost text-textSeach">Регион</span>
          <svg width="11" height="6" viewBox="0 0 11 6" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0.680298 0.374023L5.6803 5.37402L10.6803 0.374023H0.680298Z" fill="black" />
          </svg>
        </button>
        <svg width="2" height="61" viewBox="0 0 2 61" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1" height="60" rx="0.5" transform="matrix(1 -7.32621e-05 0.000207837 1 0.680298 0.374023)" fill="#D2D2D2" />
        </svg>
        <button className="bg-white py-3 px-7 inline-flex items-center focus:outline-none">
          <span className="pr-4 font-jost text-textSeach">Тип похода</span>
          <svg width="11" height="6" viewBox="0 0 11 6" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0.680298 0.374023L5.6803 5.37402L10.6803 0.374023H0.680298Z" fill="black" />
          </svg>
        </button>
        <svg width="2" height="61" viewBox="0 0 2 61" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1" height="60" rx="0.5" transform="matrix(1 -7.32621e-05 0.000207837 1 0.680298 0.374023)" fill="#D2D2D2" />
        </svg>
        <button className="bg-white py-3 px-7 inline-flex items-center focus:outline-none">
          <span className="pr-4 font-jost text-textSeach">Сложность</span>
          <svg width="11" height="6" viewBox="0 0 11 6" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0.680298 0.374023L5.6803 5.37402L10.6803 0.374023H0.680298Z" fill="black" />
          </svg>
        </button>
        <svg width="2" height="61" viewBox="0 0 2 61" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1" height="60" rx="0.5" transform="matrix(1 -7.32621e-05 0.000207837 1 0.680298 0.374023)" fill="#D2D2D2" />
        </svg>
        <button className="bg-white py-3 px-7 inline-flex items-center focus:outline-none">
          <span className="pr-4 font-jost text-textSeach">Дата</span>
          <svg width="19" height="21" viewBox="0 0 19 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.90692 9.36328H4.90692V11.3633H6.90692V9.36328ZM10.9069 9.36328H8.90692V11.3633H10.9069V9.36328ZM14.9069 9.36328H12.9069V11.3633H14.9069V9.36328ZM16.9069 2.36328H15.9069V0.363281H13.9069V2.36328H5.90692V0.363281H3.90692V2.36328H2.90692C1.79692 2.36328 0.906921 3.26328 0.906921 4.36328V18.3633C0.906921 18.8937 1.11763 19.4024 1.49271 19.7775C1.86778 20.1526 2.37649 20.3633 2.90692 20.3633H16.9069C17.4374 20.3633 17.9461 20.1526 18.3211 19.7775C18.6962 19.4024 18.9069 18.8937 18.9069 18.3633V4.36328C18.9069 3.83285 18.6962 3.32414 18.3211 2.94907C17.9461 2.57399 17.4374 2.36328 16.9069 2.36328ZM16.9069 18.3633H2.90692V7.36328H16.9069V18.3633Z" fill="black" />
          </svg>
        </button>
        <svg width="2" height="61" viewBox="0 0 2 61" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1" height="60" rx="0.5" transform="matrix(1 -7.32621e-05 0.000207837 1 0.680298 0.374023)" fill="#D2D2D2" />
        </svg>
        <button className="bg-white py-3 px-7 inline-flex items-center focus:outline-none">
          <span className="pr-4 font-jost text-textSeach">Цена</span>
          <svg width="11" height="6" viewBox="0 0 11 6" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0.680298 0.374023L5.6803 5.37402L10.6803 0.374023H0.680298Z" fill="black" />
          </svg>
        </button>
        <button className="bg-gray-400 py-3 px-7 inline-flex items-center rounded-r-lg focus:outline-none">
          <span className="font-jost px-7 font-bold text-textSeach">Найти</span>
          </button>
      </div>
    </div>
  );
};

export default Search
