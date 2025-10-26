import React from 'react';
import ServicesList from '../../components/services/ServicesList';

const ServicesPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Наши услуги</h1>
      <ServicesList />
    </div>
  );
};

export default ServicesPage;