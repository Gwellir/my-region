import React from "react"
import arrowLeft from "../../images/icons/arrowLeft.png"
import arrowRight from "../../images/icons/arrowRight.png"

const Reviews = () => {
    return (
        <div className="w-auto bg-secondary pb-16">
            <span className="flex justify-center font-bold font-jost text-xl pt-11 pb-12">Отзывы</span>
            <div className="flex items-center justify-around">
                <img className=" w-12 h-12 " src={arrowLeft} alt="arrowLeft" />
                <div className="flex flex-col w-1/3 bg-primary rounded-xl p-8">
                    <span className="text-titleReviews font-jost font-bold pb-2">Зимний тур в Териберку</span>
                    <span className="text-dateReviewesSize font-jost text-dateReviewes pb-2.5">17.08.21-21.08.21</span>
                    <span className="font-jost text-textSeach pb-5">Матвей Миронов</span>
                    <p className="font-jost text-pReviews pb-6">Отдохнул отлично, перезагрузился. Тур покупал в последний момент, чтобы убежать на юг из холодной Москвы. Про Египет не знал ничего кроме пирамид. Луксор с его древними храмами вообще оказался для меня полным сюрпризом. </p>
                    <div>
                        <span className="font-jost text-textSeach">Сложность: </span>
                        <span className="font-jost text-textSeach font-medium">Тяжело</span>
                    </div>
                    <div>
                        <span className="font-jost text-textSeach">Инструктор: </span>
                        <span className="font-jost text-textSeach font-medium">Понравился</span>
                    </div>
                    <div>
                        <span className="font-jost text-textSeach">Общая оценка: </span>
                        <span className="font-jost text-textSeach font-medium">Хорошо</span>
                    </div>
                </div>
                <div className="flex flex-col w-1/3 bg-primary rounded-xl p-8">
                    <span className="text-titleReviews font-jost font-bold pb-2">Зимний тур в Териберку</span>
                    <span className="text-dateReviewesSize font-jost text-dateReviewes pb-2.5">17.08.21-21.08.21</span>
                    <span className="font-jost text-textSeach pb-5">Матвей Миронов</span>
                    <p className="font-jost text-pReviews pb-6">Отдохнул отлично, перезагрузился. Тур покупал в последний момент, чтобы убежать на юг из холодной Москвы. Про Египет не знал ничего кроме пирамид. Луксор с его древними храмами вообще оказался для меня полным сюрпризом. </p>
                    <div>
                        <span className="font-jost text-textSeach">Сложность: </span>
                        <span className="font-jost text-textSeach font-medium">Тяжело</span>
                    </div>
                    <div>
                        <span className="font-jost text-textSeach">Инструктор: </span>
                        <span className="font-jost text-textSeach font-medium">Понравился</span>
                    </div>
                    <div>
                        <span className="font-jost text-textSeach">Общая оценка: </span>
                        <span className="font-jost text-textSeach font-medium">Хорошо</span>
                    </div>
                </div>
                <img className="w-12 h-12" src={arrowRight} alt="arrowRight" />
            </div>
        </div>
    )
}

export default Reviews