import React from 'react';

const ContactsPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Контакты</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-2xl font-semibold mb-4">Наши контакты</h2>
          <div className="space-y-4">
            <div>
              <h3 className="font-medium">Адрес:</h3>
              <p className="text-gray-600">г. Москва, ул. Примерная, д. 123</p>
            </div>
            <div>
              <h3 className="font-medium">Телефон:</h3>
              <p className="text-gray-600">+7 (999) 123-45-67</p>
            </div>
            <div>
              <h3 className="font-medium">Email:</h3>
              <p className="text-gray-600">info@evias.ru</p>
            </div>
            <div>
              <h3 className="font-medium">Часы работы:</h3>
              <p className="text-gray-600">Пн-Пт: 9:00 - 20:00</p>
              <p className="text-gray-600">Сб-Вс: 10:00 - 18:00</p>
            </div>
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-2xl font-semibold mb-4">Напишите нам</h2>
          <form className="space-y-4">
            <div>
              <label className="block text-gray-700 mb-2">Ваше имя</label>
              <input
                type="text"
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div>
              <label className="block text-gray-700 mb-2">Email</label>
              <input
                type="email"
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div>
              <label className="block text-gray-700 mb-2">Сообщение</label>
              <textarea
                className="w-full p-2 border rounded"
                rows="4"
                required
              />
            </div>
            <button
              type="submit"
              className="bg-primary text-white px-6 py-2 rounded hover:bg-primary-dark"
            >
              Отправить
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ContactsPage;