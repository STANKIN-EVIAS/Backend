import React from 'react';
import SymptomsList from '../../components/symptoms/SymptomsList';

const SymptomsPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Симптомы</h1>
      <p className="text-gray-600 mb-6">
        Здесь вы можете найти информацию о различных симптомах у животных и получить
        рекомендации по первой помощи. Помните, что эта информация не заменяет
        консультацию с ветеринарным врачом.
      </p>
      <SymptomsList />
    </div>
  );
};

export default SymptomsPage;