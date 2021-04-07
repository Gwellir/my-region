import React from 'react'

const getFire = () => {
    let content = [];
    for (let i = 0; i < 5; i++) {
        if (i < 3) {
            content.push(
                <svg width="15" height="19" viewBox="0 0 15 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13.7752 10.2685C12.432 6.78083 7.64945 6.59277 8.80445 1.52368C8.89001 1.14756 8.4879 0.856922 8.16278 1.05353C5.05713 2.88285 2.82413 6.55003 4.69779 11.3541C4.85179 11.7473 4.38979 12.1149 4.05613 11.8585C2.50758 10.6874 2.34502 9.00337 2.48191 7.79807C2.53324 7.35356 1.95147 7.13986 1.70336 7.50743C1.12158 8.39644 0.53125 9.83254 0.53125 11.9952C0.85636 16.7822 4.90313 18.2525 6.35757 18.4406C8.43656 18.7056 10.6867 18.3209 12.3037 16.8421C14.0832 15.1923 14.7334 12.5594 13.7752 10.2685ZM5.83568 14.5683C7.06768 14.2691 7.70079 13.3801 7.8719 12.5936C8.15423 11.3712 7.05057 10.1745 7.7949 8.24258C8.07723 9.84109 10.5926 10.8412 10.5926 12.5851C10.661 14.7478 8.31678 16.6027 5.83568 14.5683Z" fill="#7C0202" />
                </svg>
            );
        }
        else {
            content.push(
                <svg width="14" height="19" viewBox="0 0 14 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M13.3748 10.2685C12.0316 6.78083 7.24906 6.59277 8.40406 1.52368C8.48961 1.14756 8.0875 0.856922 7.76239 1.05353C4.65674 2.88285 2.42374 6.55003 4.2974 11.3541C4.4514 11.7473 3.9894 12.1149 3.65574 11.8585C2.10719 10.6874 1.94463 9.00337 2.08152 7.79807C2.13285 7.35356 1.55108 7.13986 1.30297 7.50743C0.721191 8.39644 0.130859 9.83254 0.130859 11.9952C0.45597 16.7822 4.50274 18.2525 5.95718 18.4406C8.03617 18.7056 10.2863 18.3209 11.9033 16.8421C13.6828 15.1923 14.333 12.5594 13.3748 10.2685ZM5.43529 14.5683C6.66729 14.2691 7.3004 13.3801 7.47151 12.5936C7.75384 11.3712 6.65017 10.1745 7.39451 8.24258C7.67684 9.84109 10.1922 10.8412 10.1922 12.5851C10.2606 14.7478 7.91639 16.6027 5.43529 14.5683Z" fill="#7C0202" fill-opacity="0.5" />
                </svg>
            )
        }
    }
    return content;
};

const RouteDetailInfo = () => {
    return (
        <div className="rounded-md bg-bgInfo pt-4">
            <span className="font-jostmd pl-6 text-addressSize">Основная информация</span>
            <div>
                <div className="flex  pt-2.5">
                    <div className="flex flex-col pl-7 pr-11">
                        <span className="font-jostmd text-textGrey text-detailSize">Тип</span>
                        <span className="font-jostmd text-titleRegister">Пеший</span>
                        <span className="font-jostmd text-textGrey text-detailSize pt-3">Длина маршрута</span>
                        <span className="font-jostmd text-titleRegister">27.0 км</span>
                    </div>
                    <div className="flex flex-col pb-8">
                        <span className="font-jostmd text-textGrey text-detailSize">Длительность</span>
                        <span className="font-jostmd text-titleRegister">1 день</span>
                        <span className="font-jostmd text-textGrey text-detailSize pt-3">Сложность</span>
                    <div className="flex">{getFire()}</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default RouteDetailInfo