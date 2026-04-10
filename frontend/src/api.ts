import axios from 'axios';

// Адреса нашого Python сервера
const API_URL = 'http://127.0.0.1:8000/api';

export const getStatus = () => axios.get(`${API_URL}/status`);
export const getConfig = () => axios.get(`${API_URL}/config`);
export const startWinding = () => axios.post(`${API_URL}/start`);
export const stopWinding = () => axios.post(`${API_URL}/stop`);