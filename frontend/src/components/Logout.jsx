import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { logout } from '../api/auth';

const Logout = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const performLogout = async () => {
            try {
                await logout(); // Вызов API для выхода
                localStorage.removeItem('token'); // Удаляем токен из localStorage
                navigate('/login'); // Перенаправляем на страницу входа
            } catch (error) {
                console.error('Ошибка при выходе:', error);
                navigate('/login');
            }
        };

        performLogout();
    }, [navigate]);

    return null; // Компонент ничего не рендерит
};

export default Logout;