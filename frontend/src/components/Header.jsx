import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { getProfile } from "../api/profile";

export default function Header() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    getProfile()
      .then(setUser)
      .catch(console.error);
  }, []);

  return (
    <header className="bg-neutral-100 shadow-md relative">
      {/* Верхняя часть: логотип и контакты */}
      <div className="container mx-auto flex justify-between items-center h-28 px-6">
        <Link to="/">
          <div>
            <h1 className="text-5xl font-black font-inter">ЕВИАС</h1>
            <p className="text-xs text-gray-500 mt-1">
              Единая ветеринарная информационно-аналитическая система
            </p>
          </div>
        </Link>
        <div className="flex items-center gap-4">
          <p className="text-sm text-gray-600">+7 (999) 123-45-67</p>
          <CallDoctorButton />
          <OnlineBookingButton />
          <ProfileButton user={user} />
        </div>
      </div>
      {/* Нижняя навигация */}
      <nav className="bg-white shadow-[0px_6px_4px_rgba(0,0,0,0.59)]">
        <div className="container mx-auto flex justify-center gap-8 h-16 items-center px-6">
          <NavItem text="Услуги" to="/services" />
          <NavItem text="Контакты" to="/contacts" />
          <NavItem text="Отзывы" to="/reviews" />
          <NavItem text="Ветклиники" to="/clinics" />
          <NavItem text="Симптомы" to="/symptoms" />
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

function ProfileButton({ user }) {
  const isAuth = !!user || !!localStorage.getItem("accessToken");
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    navigate("/login");
  };

  return (
    <div className="flex items-center gap-2">
      <Link
        to={isAuth ? "/profile" : "/login"}
        className="flex items-center gap-2 bg-blue-600 text-white font-medium rounded-full h-12 px-4 hover:bg-blue-700"
      >
        <div className="w-6 h-6 rounded-full overflow-hidden">
          {user?.image ? (
            <img src={user.image} alt="Аватар" className="w-full h-full object-cover" />
          ) : (
            <div className="w-full h-full bg-white"></div>
          )}
        </div>
        Личный кабинет
      </Link>
      {isAuth && (
        <a href="logout"
          className="flex items-center gap-2 bg-red-500 text-white font-medium rounded-full h-12 px-4 hover:bg-red-600"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 001 1h12a1 1 0 001-1V4a1 1 0 00-1-1H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8z" clipRule="evenodd" />
          </svg>
          Выйти
        </a>
      )}
    </div>
  );
}


function NavItem({ text, to }) {
  return (
    <Link
      to={to}
      className="text-black font-semibold hover:text-blue-600 transition"
    >
      {text}
    </Link>
  );
}
