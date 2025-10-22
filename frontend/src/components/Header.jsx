import React from "react";

export default function Header() {
  return (
    <header className="bg-neutral-100 shadow-md relative">
      {/* Верхняя часть: логотип и контакты */}
      <div className="container mx-auto flex justify-between items-center h-28 px-6">
        <div>
          <h1 className="text-5xl font-black font-inter">ЕВИАС</h1>
          <p className="text-xs text-gray-500 mt-1">
            Единая ветеринарная информационно-аналитическая система
          </p>
        </div>
        <div className="flex items-center gap-4">
          <p className="text-sm text-gray-600">+7 (ХХХ) - ХХХ- ХХ - ХХ</p>
          <CallDoctorButton />
          <OnlineBookingButton />
          <ProfileButton />
        </div>
      </div>

      {/* Нижняя навигация */}
        <nav className="bg-white shadow-xl">
        <div className="container mx-auto flex justify-center gap-8 h-16 items-center px-6">
            <NavItem text="Услуги" />
            <NavItem text="Контакты" />
            <NavItem text="Отзывы" />
            <NavItem text="Ветклиники" />
            <NavItem text="Благотворительность" />
        </div>
        </nav>
    </header>
  );
}

function CallDoctorButton() {
  return (
    <button className="bg-blue-600 text-white font-medium rounded-full h-12 px-6 hover:bg-blue-700">
      Вызвать врача на дом
    </button>
  );
}

function OnlineBookingButton() {
  return (
    <button className="bg-green-500 text-white font-medium rounded-full h-12 px-6 hover:bg-green-600">
      Записаться онлайн
    </button>
  );
}

function ProfileButton() {
  return (
    <a
      href="/login"
      className="flex items-center gap-2 bg-blue-600 text-white font-medium rounded-full h-12 px-4 hover:bg-blue-700"
    >
      <div className="w-6 h-6 bg-white rounded-full"></div>
      Личный кабинет
    </a>
  );
}

function NavItem({ text }) {
  return (
    <button className="text-black font-semibold hover:text-blue-600 transition">
      {text}
    </button>
  );
}
