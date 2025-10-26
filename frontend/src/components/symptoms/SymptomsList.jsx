import React, { useState } from 'react';

const SymptomsList = () => {
  const [symptoms] = useState([
    {
      id: 1,
      name: "Потеря аппетита",
      description: "Животное отказывается от еды или ест меньше обычного",
      urgency: "medium",
      recommendations: "Наблюдайте за питомцем 24 часа. Если аппетит не восстановится, обратитесь к ветеринару."
    },
    {
      id: 2,
      name: "Рвота",
      description: "Частая рвота или позывы к рвоте",
      urgency: "high",
      recommendations: "Немедленно обратитесь к ветеринару, особенно если рвота повторяется или содержит кровь."
    },
    {
      id: 3,
      name: "Вялость",
      description: "Необычная усталость, сонливость или апатия",
      urgency: "medium",
      recommendations: "Следите за другими симптомами и изменениями в поведении. При ухудшении состояния обратитесь к врачу."
    }
  ]);

  const [searchTerm, setSearchTerm] = useState('');

  const filteredSymptoms = symptoms.filter(symptom =>
    symptom.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    symptom.description.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const getUrgencyClass = (urgency) => {
    switch (urgency) {
      case 'high':
        return 'bg-red-100 text-red-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'low':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const getUrgencyText = (urgency) => {
    switch (urgency) {
      case 'high':
        return 'Срочно обратитесь к врачу';
      case 'medium':
        return 'Требуется консультация';
      case 'low':
        return 'Можно наблюдать';
      default:
        return 'Неопределенная срочность';
    }
  };

  return (
    <div className="p-4">
      <div className="mb-6">
        <input
          type="text"
          placeholder="Поиск симптомов..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full p-2 border rounded"
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredSymptoms.map((symptom) => (
          <div key={symptom.id} className="bg-white rounded-lg shadow p-4">
            <h3 className="text-xl font-semibold mb-2">{symptom.name}</h3>
            <p className="text-gray-600 mb-4">{symptom.description}</p>
            <div className="mb-4">
              <h4 className="font-medium mb-2">Рекомендации:</h4>
              <p className="text-gray-600">{symptom.recommendations}</p>
            </div>
            <div className="mt-4">
              <span className={`px-3 py-1 rounded-full text-sm ${getUrgencyClass(symptom.urgency)}`}>
                {getUrgencyText(symptom.urgency)}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SymptomsList;