import axios from 'axios';
import { API_URL } from './config';

export const getServices = async () => {
  try {
    const response = await axios.get(`${API_URL}/vet-clinics/services/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getServiceById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/vet-clinics/services/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
};