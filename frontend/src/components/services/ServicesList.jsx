import React, { useState, useEffect } from 'react';
import { getServices } from '../../api/services';

const ServicesList = () => {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const data = await getServices();
        setServices(data);
        setLoading(false);
      } catch (err) {
        setError('Не удалось загрузить услуги');
        setLoading(false);
      }
    };

    fetchServices();
  }, []);

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
      {services.map((service) => (
        <div key={service.id} className="bg-white rounded-lg shadow p-4">
          <h3 className="text-xl font-semibold mb-2">{service.name}</h3>
          <p className="text-gray-600 mb-2">{service.description}</p>
          <p className="text-primary font-bold">Цена: {service.price} ₽</p>
        </div>
      ))}
    </div>
  );
};

export default ServicesList;