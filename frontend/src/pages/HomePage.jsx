// src/pages/HomePage.jsx
import React from 'react';
import imgPhoto202510220002481 from "../assets/unnamed (5)-no-bg-preview (carve.photos).png";
import imgKT from "../assets/unnamed.png";
import imgSterilization from"../assets/unnamed (2)-no-bg-preview (carve.photos).png";
import imgGrooming from "../assets/unnamed (3)-no-bg-preview (carve.photos).png";
import imgFriend from "../assets/Gemini_Generated_Image_8vmpnz8vmpnz8vmp-no-bg-preview (carve.photos).png";
import charityAnimal from '../assets/unnamed (7)-edited-free (carve.photos) (9).png';
import registrationPet from '../assets/unnamed (4)-no-bg-preview (carve.photos).png';



// Компонент кнопки "Подробнее"
function Frame39() {
  return (
    <button className="detail-button">
      <div className="detail-button-text">
        <p>Подробнее</p>
      </div>
    </button>
  );
}

// Компонент карточки консультации
function ConsultationCard() {
  return (
    <div className="consultation-card">
      <div className="consultation-title">
        <p>Бесплатная первая онлайн консультация врача</p>
      </div>
      <div className="consultation-image">
        <img 
          alt="Ветеринарный врач" 
          src={imgPhoto202510220002481} 
        />
      </div>
      <div className="consultation-description">
        <p>успей проконсультароваться со специалистом до 31 ноября</p>
      </div>
      <Frame39 />
    </div>
  );
}

function AdditionalCard({ title, color, image }) {
  return (
    <div className={`additional-card ${color}`}>
      <div className="card-title">
        <p>{title}</p>
      </div>
      <div className="card-image">
        <img alt={title} src={image} />
      </div>
      <button className="detail-button">
        <div className="detail-button-text">
          <p>Подробнее</p>
        </div>
      </button>
    </div>
  );
}

// Компонент кнопки с кружком
const ButtonWithArrow = ({ children }) => (
  <button className="button-with-arrow">
    {children}
    <div className="arrow-circle">
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
    <div className="homepage-container">
      <div className="homepage-inner">
        
        {/* Блок 1 */}
        <div className="content-block">
          <div className="content-text">
            <p className="text-justify">
              <strong>Единая Ветеринарная Информационно-Аналитическая Система (ЕВИАС)</strong> — 
              это централизованная цифровая платформа, созданная для комплексного решения задач 
              в сфере ветеринарии и заботы о здоровье животных.
            </p>
          </div>
          
          <div className="photo-circle">
            <img 
              src="https://hub.ldpr.ru/media/images/magadan/3e34a4c270d2a872892831b55440c39cd96cfb5377c9049135983019895d39fa.jpg" 
              alt="Ветеринар с животным"
            />
          </div>
        </div>

        {/* Блок 2 */}
        <div className="content-block ">
          <div className="photo-circle">
            <img 
              src="https://i.pinimg.com/originals/3b/3c/28/3b3c28137cf09cce59018d5c2128e78c.jpg" 
              alt="Веселая собачка"
            />
          </div>
          
          <div className="content-text">
            <p className="text-justify">
              Система объединяет владельцев домашних животных, ветеринарных врачей, клиники и государственные контролирующие органы, 
              обеспечивая слаженное взаимодействие между всеми участниками процесса. Благодаря ЕВИАС владельцы животных получают удобный 
              доступ к записи на приёмы, ведению цифровых медицинских карт питомцев и истории их лечения.
            </p>
          </div>
        </div>

        {/* Блок 3 */}
        <div className="content-block ">
          <div className="content-text">
            <p className="text-justify">
              Ветеринарные специалисты и клиники используют платформу для автоматизации рабочего процесса, 
              ведения документации и быстрого обмена информацией. На уровне государства система позволяет 
              осуществлять мониторинг отрасли, контролировать эпидемиологическую обстановку и повышать общие 
              стандарты ветеринарного обслуживания.
            </p>
          </div>
          
          <div className="photo-circle">
            <img 
              src="https://avatars.mds.yandex.net/get-altay/13524363/2a00000192ae8f7b41f221d17ace42e9df50/orig" 
              alt="Недовольный кот с ветеринаром"
            />
          </div>
        </div>

        {/* Блок с картой и кнопками */}
<div className="map-section">
  <h2 className="map-title">
    Что вас интересует?
  </h2>

  <div className="map-buttons-wrapper">
    
        {/* Левая часть - интерактивная карта */}
        <div className="map-wrapper">
          <div className="map-container">
            <iframe 
              src="https://yandex.ru/map-widget/v1/?um=constructor%3AYourMapCode"
              className="map-iframe"
              title="Интерактивная карта"
            />
          </div>
        </div>

        {/* Правая часть - кнопки */}
        <div className="buttons-wrapper">
          <ButtonWithArrow>Ветклиники</ButtonWithArrow>
          <div className="buttons-row">
            <ButtonWithArrow>Диагностика</ButtonWithArrow>
            <ButtonWithArrow>Анализы</ButtonWithArrow>
          </div>
          <div className="buttons-row">
            <ButtonWithArrow>Заболевания</ButtonWithArrow>
            <ButtonWithArrow>Симптомы</ButtonWithArrow>
          </div>
        </div>

      </div>
    </div>

<div className="promotions-section">
  <h2 className="promotions-title">
    Специальные предложения и акции
  </h2>
        {/* Карточки с акциями */}
        <div className="cards-container">
          
          <div className="main-card-container">
            <ConsultationCard />
          </div>
          <div className="small-cards-container">
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
        <div className="all-promotions-button-container">
          <button className="all-promotions-button">
            Все акции и предложения
          </button>
        </div>
      </div>

      <div className="charity-section">
        <h2 className="charity-title">Благотворительность</h2>
        
        <div className="charity-card">
          {/* Заголовок внутри карточки */}
          <div className="charity-main-title">
            <p>Помоги бездомным животным</p>
          </div>
          
          {/* Изображение животного */}
          <div className="charity-image">
            {/* ЗАМЕНИТЕ ЭТУ ССЫЛКУ НА ПУТЬ ДО ВАШЕГО ИЗОБРАЖЕНИЯ */}
            <img 
              src={charityAnimal} 
              alt="Бездомное животное, нуждающееся в помощи"
            />
          </div>
          
          {/* Кнопка пожертвования */}
          <button className="charity-button">
            <div className="charity-button-text">
              <p>Сделать пожертвование</p>
            </div>
          </button>
          
          {/* Описание */}
          <p className="charity-description">
            Вместе с ЕВИАС мы создаем не просто технологичную среду для питомцев, 
            но и поддерживаем тех, кто в ней больше всего нуждается. Ваши пожертвования 
            направляются на лечение и содержание животных из приютов, помогая им 
            обрести здоровье и новую семью.
          </p>
        </div>
      </div>

      {/* Карточка регистрации */}
      <div className="registration-section">
        <h2 className="registration-title">Регистрация</h2>
        
        <div className="registration-card">
          {/* Главный заголовок */}
          <div className="registration-main-title">
            <p>Мы вам поможем!</p>
          </div>
          
          {/* Подзаголовок */}
          <div className="registration-subtitle">
            <p>Зарегистрируйтесь на нашем сайте и вы сможете записаться на встречу со специалистом или получить первую бесплатную онлайн консультацию</p>
          </div>
          
          {/* Поле для имени */}
          <div className="registration-input name">
            <div className="registration-input-text">
              <p>Фамилия Имя Отчество</p>
            </div>
          </div>
          
          {/* Поле для email */}
          <div className="registration-input email">
            <div className="registration-input-text">
              <p>email</p>
            </div>
          </div>
          
          {/* Чекбокс */}
          <div className="registration-checkbox"></div>
          <div className="registration-checkbox-label">
            <p>Я согласен(а) на обработку персональных данных</p>
          </div>
          
          {/* Кнопка регистрации */}
          <button className="registration-button">
            <div className="registration-button-text">
              <p>Зарегистрироваться</p>
            </div>
          </button>
          
          {/* Изображение */}
          <div className="registration-image">
            
            <img 
              src={registrationPet}
              alt="Домашний питомец"
            />
          </div>
        </div>
      </div>
        
      </div>
    </div>
  );
};

export default HomePage;