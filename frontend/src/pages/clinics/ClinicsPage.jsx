import React from 'react';
import ClinicsList from '../../components/clinics/ClinicsList';

const ClinicsPage = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Ветеринарные клиники</h1>
      <ClinicsList />
    </div>
  );
};

export default ClinicsPage;