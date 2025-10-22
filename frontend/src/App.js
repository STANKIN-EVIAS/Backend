import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Profile from "./components/Profile";
import Header from "./components/Header";
import HomePage from "./pages/HomePage"; // Добавьте этот импорт
import './App.css';

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/" element={<HomePage />} /> {/* Заменили на компонент HomePage */}
      </Routes>
    </BrowserRouter>
  );
}