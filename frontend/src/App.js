import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Profile from "./pages/UserProfilePage";
import Header from "./components/Header";
import './App.css';

export default function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/" element={<h1 className="text-center mt-10 text-2xl">Главная страница</h1>} />
      </Routes>
    </BrowserRouter>
  );
}
