import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import ProfilePage from "./pages/UserProfilePage";
import Header from "./components/Header";
import HomePage from "./pages/HomePage";
import Logout from "./components/Logout";
import './App.css';

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/" element={<HomePage />} /> {/* Заменили на компонент HomePage */}
      </Routes>
    </BrowserRouter>
  );
}