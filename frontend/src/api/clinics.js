import axios from 'axios';
import { API_URL } from './config';

export const getClinics = async () => {
  try {
    const response = await axios.get(`${API_URL}/vet-clinics/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getClinicById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/vet-clinics/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getClinicAppointments = async (clinicId) => {
  try {
    const response = await axios.get(`${API_URL}/vet-clinics/${clinicId}/appointments/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};