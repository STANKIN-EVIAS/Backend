import React, { useState, useEffect } from 'react';
import { getClinics } from '../../api/clinics';

const ClinicsList = () => {
  const [clinics, setClinics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchClinics = async () => {
      try {
        const data = await getClinics();
        setClinics(data);
        setLoading(false);
      } catch (err) {
        setError('Не удалось загрузить список клиник');
        setLoading(false);
      }
    };

    fetchClinics();
  }, []);

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
      {clinics.map((clinic) => (
        <div key={clinic.id} className="bg-white rounded-lg shadow p-6">
          <h3 className="text-xl font-semibold mb-2">{clinic.name}</h3>
          <p className="text-gray-600 mb-4">{clinic.address}</p>
          <div className="mb-4">
            <h4 className="font-medium mb-2">Часы работы:</h4>
            <p className="text-gray-600">
              {clinic.working_hours}
            </p>
          </div>
          <div className="mb-4">
            <h4 className="font-medium mb-2">Контакты:</h4>
            <p className="text-gray-600">
              Телефон: {clinic.phone}
            </p>
            {clinic.email && (
              <p className="text-gray-600">
                Email: {clinic.email}
              </p>
            )}
          </div>
          <button className="bg-primary text-white px-4 py-2 rounded hover:bg-primary-dark">
            Записаться на прием
          </button>
        </div>
      ))}
    </div>
  );
};

export default ClinicsList;