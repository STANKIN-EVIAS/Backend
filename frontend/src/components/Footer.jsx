import React from "react";
import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="bg-neutral-100 shadow-md relative py-8">
      <div className="container mx-auto px-6">
        <div className="flex justify-between items-start">
          {/* Левая часть: логотип и текст справа от него */}
          <div className="flex items-start gap-8">
            {/* Логотип */}
            <div>
              <h1 className="text-5xl font-black font-inter">ЕВИАС</h1>
              <p className="text-xs text-gray-500 mt-1">
                Единая ветеринарная информационно-аналитическая система
              </p>
            </div>
            
            {/* Текст справа от логотипа */}
            <div className="text-sm text-gray-600 space-y-1">
              <p className="mb-0">© 2025, ЕВИАС</p>
              <p className="mb-0">Юридическая информация:</p>
              <p className="mb-0">Адрес:</p>
              <p className="mb-0">При возникновении любых технических сложностей сообщите нам по почте:</p>
              <p className="text-blue-600">email@mail.com</p>
            </div>
          </div>

          {/* Правая часть: ссылки */}
          <div className="text-right space-y-2">
            <Link 
              to="/privacy-policy" 
              className="block text-sm text-gray-600 hover:text-blue-600 transition"
            >
              Политика конфиденциальности
            </Link>
            <Link 
              to="/personal-data" 
              className="block text-sm text-gray-600 hover:text-blue-600 transition"
            >
              Согласие на обработку персональных данных
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
}