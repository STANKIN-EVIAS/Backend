import React, { useState, useEffect } from 'react';

const ReviewsList = () => {
  const [reviews, setReviews] = useState([
    {
      id: 1,
      author: "Иван Петров",
      text: "Отличная клиника! Очень внимательный персонал.",
      rating: 5,
      date: "2025-10-25"
    },
    {
      id: 2,
      author: "Мария Иванова",
      text: "Быстро приняли, профессионально помогли нашему питомцу.",
      rating: 4,
      date: "2025-10-24"
    }
  ]);

  return (
    <div className="space-y-4">
      {/* Форма добавления отзыва */}
      <div className="bg-white rounded-lg shadow p-4 mb-6">
        <h3 className="text-lg font-semibold mb-4">Оставить отзыв</h3>
        <form className="space-y-4">
          <div>
            <textarea
              className="w-full p-2 border rounded"
              rows="4"
              placeholder="Ваш отзыв..."
            ></textarea>
          </div>
          <div className="flex items-center gap-2">
            <span>Оценка:</span>
            <select className="border rounded p-1">
              <option>5</option>
              <option>4</option>
              <option>3</option>
              <option>2</option>
              <option>1</option>
            </select>
          </div>
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Отправить
          </button>
        </form>
      </div>

      {/* Список отзывов */}
      {reviews.map((review) => (
        <div key={review.id} className="bg-white rounded-lg shadow p-4">
          <div className="flex justify-between items-start mb-2">
            <div>
              <h3 className="font-semibold">{review.author}</h3>
              <div className="flex items-center">
                <div className="flex text-yellow-400">
                  {[...Array(review.rating)].map((_, i) => (
                    <span key={i}>★</span>
                  ))}
                </div>
                <span className="text-gray-500 text-sm ml-2">{review.date}</span>
              </div>
            </div>
          </div>
          <p className="text-gray-600">{review.text}</p>
        </div>
      ))}
    </div>
  );
};

export default ReviewsList;