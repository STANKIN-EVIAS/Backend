// src/pages/HomePage.jsx
import React from 'react';
import imgPhoto202510220002481 from "../assets/unnamed (5)-no-bg-preview (carve.photos).png";
import imgKT from "../assets/unnamed.png";
import imgSterilization from"../assets/unnamed (2)-no-bg-preview (carve.photos).png";
import imgGrooming from "../assets/unnamed (3)-no-bg-preview (carve.photos).png";
import imgFriend from "../assets/Gemini_Generated_Image_8vmpnz8vmpnz8vmp-no-bg-preview (carve.photos).png";

// Компонент кнопки "Подробнее"
function Frame39() {
  return (
    <button className="absolute bg-white bottom-[16px] h-[32px] left-[29px] overflow-clip rounded-[25px] w-[113px] cursor-pointer hover:bg-gray-100 transition duration-300">
      <div className="absolute bottom-[8px] flex flex-col font-['Inter:Light',_sans-serif] font-light justify-center leading-[0] left-1/2 not-italic text-[12px] text-black text-center top-[8px] tracking-[-0.06px] translate-x-[-50%] w-[79px]">
        <p className="leading-[1.45]">Подробнее</p>
      </div>
    </button>
  );
}

// Компонент карточки консультации
function ConsultationCard() {
  return (
    <div className="bg-[rgba(80,196,59,0.91)] overflow-clip relative rounded-[25px] shadow-[0px_4px_4px_0px_rgba(0,0,0,0.25)] h-[300px] min-w-[450px]">
      <div className="absolute flex flex-col font-['Inter:Semi_Bold',_sans-serif] font-semibold h-[105px] justify-center leading-[0] left-[27px] not-italic text-[24px] text-white top-[75.5px] tracking-[-0.12px] translate-y-[-50%] w-[283px]">
        <p className="leading-[1.45]">{`Бесплатная первая онлайн консультация врача `}</p>
      </div>
      <div className="absolute aspect-[300/347] bottom-[-26px] right-[-6px] top-[14px]" data-name="photo_2025-10-22_00-02-48 1">
        <img 
          alt="Ветеринарный врач" 
          className="absolute inset-0 max-w-none object-50%-50% object-cover pointer-events-none size-full" 
          src={imgPhoto202510220002481} 
        />
      </div>
      <div className="absolute flex flex-col font-['Inter:Light',_sans-serif] font-light h-[39px] justify-center leading-[0] left-[27px] not-italic text-[12px] text-white top-[168.5px] tracking-[-0.06px] translate-y-[-50%] w-[187px]">
        <p className="leading-[1.45]">успей проконсультароваться со специалистом до 31 ноября</p>
      </div>
      <Frame39 />
    </div>
  );
}

function AdditionalCard({ title, color, image }) {
  return (
    <div className={`${color} overflow-clip relative rounded-[25px] h-[143px] min-w-[150px] shadow-[0px_4px_4px_0px_rgba(0,0,0,0.25)]`}>
      {/* Текст */}
      <div className="absolute flex flex-col font-['Inter:Semi_Bold',_sans-serif] font-semibold justify-center leading-[0] left-[15px] not-italic text-[14px] text-white top-[20px] tracking-[-0.07px] w-[70%]">
        <p className="leading-[1.4]">{title}</p>
      </div>
      
      {/* Картинка */}
      <div className="absolute aspect-square bottom-[-10px] right-[-10px] top-auto w-[80px] opacity-90">
        <img 
          alt={title} 
          className="absolute inset-0 max-w-none object-cover pointer-events-none size-full rounded-lg" 
          src={image} 
        />
      </div>
      
      {/* Кнопка Подробнее - ИЗМЕНИТЕ ШИРИНУ ЗДЕСЬ */}
      <button className="absolute bg-white bottom-[12px] h-[28px] left-[15px] overflow-clip rounded-[20px] w-[90px] cursor-pointer hover:bg-gray-100 transition duration-300">
        <div className="absolute flex flex-col font-['Inter:Light',_sans-serif] font-light justify-center leading-[0] left-1/2 not-italic text-[11px] text-black text-center top-1/2 tracking-[-0.05px] translate-x-[-50%] translate-y-[-50%] w-[80px]">
          <p className="leading-[1.4]">Подробнее</p>
        </div>
      </button>
    </div>
  );
}

// 🔧 Выносим компонент кнопки с кружком
const ButtonWithArrow = ({ children }) => (
  <button className="flex-1 hover:text-blue-500 text-black font-semibold py-11 px-10 rounded-2xl transition duration-300 text-lg shadow-xl text-left relative pr-16">
    {children}
    <div className="absolute right-4 top-1/2 transform -translate-y-1/2 size-[45px]">
      <svg className="block size-full" fill="none" viewBox="0 0 45 45">
        <circle cx="22.5" cy="22.5" fill="#50C43B" r="22.5" />
      </svg>
      <div className="absolute inset-2 flex items-center justify-center">
        <svg className="w-2 h-4" fill="none" viewBox="0 0 12 19">
          <path 
            d="M1 1L11 9.5L1 18" 
            stroke="white" 
            strokeWidth="3" 
            strokeLinecap="round" 
            strokeLinejoin="round"
          />
        </svg>
      </div>
    </div>
  </button>
);

const HomePage = () => {
  return (
    <div className="min-h-screen py-15">
      <div className="mx-auto px-20 max-w-8xl">
        
        {/* Блок 1 */}
        <div className="flex flex-col md:flex-row items-center gap-20 bg-white rounded-xl p-10">
          <div className="flex-1">
            <p className="text-xl text-gray-800 leading-relaxed text-justify">
              <strong>Единая Ветеринарная Информационно-Аналитическая Система (ЕВИАС)</strong> — 
              это централизованная цифровая платформа, созданная для комплексного решения задач 
              в сфере ветеринарии и заботы о здоровье животных.
            </p>
          </div>
          
          <div className="flex-shrink-0">
            <div className="w-96 h-96 rounded-full overflow-hidden">
              <img 
                src="https://hub.ldpr.ru/media/images/magadan/3e34a4c270d2a872892831b55440c39cd96cfb5377c9049135983019895d39fa.jpg" 
                alt="Ветеринар с животным"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>

        {/* Блок 2 */}
        <div className="flex flex-col md:flex-row items-center gap-20 bg-white rounded-xl p-10 -mt-32">
          <div className="flex-shrink-0">
            <div className="w-96 h-96 rounded-full overflow-hidden">
              <img 
                src="https://i.pinimg.com/originals/3b/3c/28/3b3c28137cf09cce59018d5c2128e78c.jpg" 
                alt="Веселая собачка"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
          
          <div className="flex-1">
            <p className="text-xl text-gray-800 leading-relaxed text-justify">
              Система объединяет владельцев домашних животных, ветеринарных врачей, клиники и государственные контролирующие органы, 
              обеспечивая слаженное взаимодействие между всеми участниками процесса. Благодаря ЕВИАС владельцы животных получают удобный 
              доступ к записи на приёмы, ведению цифровых медицинских карт питомцев и истории их лечения.
            </p>
          </div>
        </div>

        {/* Блок 3 */}
        <div className="flex flex-col md:flex-row items-center gap-20 bg-white rounded-xl p-10 -mt-32">
          <div className="flex-1">
            <p className="text-xl text-gray-800 leading-relaxed text-justify">
              Ветеринарные специалисты и клиники используют платформу для автоматизации рабочего процесса, 
              ведения документации и быстрого обмена информацией. На уровне государства система позволяет 
              осуществлять мониторинг отрасли, контролировать эпидемиологическую обстановку и повышать общие 
              стандарты ветеринарного обслуживания.
            </p>
          </div>
          
          <div className="flex-shrink-0">
            <div className="w-96 h-96 rounded-full overflow-hidden">
              <img 
                src="https://avatars.mds.yandex.net/get-altay/13524363/2a00000192ae8f7b41f221d17ace42e9df50/orig" 
                alt="Недовольный кот с ветеринаром"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        </div>

        {/* Блок с картой и кнопками */}
        <div className="mt-20 bg-white rounded-xl p-8 -mt-32">
          <h2 className="text-3xl font-bold text-gray-800 mb-8 text-left">
            Что вас интересует?
          </h2>

          <div className="flex flex-col lg:flex-row gap-8">
            
            {/* Левая часть - интерактивная карта */}
            <div className="flex-1">
                <div className="bg-gray-200 rounded-xl h-96 overflow-hidden">
                    <iframe 
                    src="https://yandex.ru/map-widget/v1/?um=constructor%3AYourMapCode"
                    width="100%" 
                    height="100%"
                    frameBorder="0"
                    title="Интерактивная карта"
                    />
                </div>
                </div>

            {/* Правая часть - кнопки */}
            <div className="flex-1 flex flex-col gap-4">
              
              {/* Первый уровень - Ветклиники */}
              <ButtonWithArrow>Ветклиники</ButtonWithArrow>

              {/* Второй уровень - Диагностика и Анализы */}
              <div className="flex gap-4">
                <ButtonWithArrow>Диагностика</ButtonWithArrow>
                <ButtonWithArrow>Анализы</ButtonWithArrow>
              </div>

              {/* Третий уровень - Заболевания и Симптомы */}
              <div className="flex gap-4">
                <ButtonWithArrow>Заболевания</ButtonWithArrow>
                <ButtonWithArrow>Симптомы</ButtonWithArrow>
              </div>

            </div>

          </div>

        </div>

        <div className="mt-12 flex justify-center gap-8">
        <div className="w-1/2">
          <ConsultationCard />
        </div>
        <div className="w-2/5 grid grid-cols-2 gap-3">
          <AdditionalCard 
            title="Скидка 20% на КТ" 
            color="bg-[rgba(59,132,196,0.82)]" 
            image={imgKT}
          />
          <AdditionalCard 
            title="Скидка на кастрацию и стерилизацию" 
            color="bg-[rgba(196,59,159,0.82)]" 
            image={imgSterilization}
          />
          <AdditionalCard 
            title="Скидка 5% на груминг собак" 
            color="bg-[rgba(196,144,59,0.82)]" 
            image={imgGrooming}
          />
          <AdditionalCard 
            title="Приведи друга и получи скидку" 
            color="bg-[rgba(59,196,100,0.82)]" 
            image={imgFriend}
          />
          </div>
        </div>


        
      </div>
    </div>
  );
};

export default HomePage;