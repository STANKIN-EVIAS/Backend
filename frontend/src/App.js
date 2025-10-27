import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import ProfilePage from "./pages/UserProfilePage";
import Header from "./components/Header";
import Footer from "./components/Footer"; // Импортируйте ваш футтер
import HomePage from "./pages/HomePage";
import ServicesPage from "./pages/services/ServicesPage";
import ContactsPage from "./pages/contacts/ContactsPage";
import ReviewsPage from "./pages/reviews/ReviewsPage";
import ClinicsPage from "./pages/clinics/ClinicsPage";
import SymptomsPage from "./pages/symptoms/SymptomsPage";
import Logout from "./components/Logout";
import './App.css';


export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50 flex flex-col">
        <Header />
        <main className="flex-grow pb-8">
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/profile" element={<ProfilePage />} />
            <Route path="/services" element={<ServicesPage />} />
            <Route path="/contacts" element={<ContactsPage />} />
            <Route path="/reviews" element={<ReviewsPage />} />
            <Route path="/clinics" element={<ClinicsPage />} />
            <Route path="/symptoms" element={<SymptomsPage />} />
            <Route path="/" element={<HomePage />} />
            <Route path="/logout" element={<Logout />} />
          </Routes>
        </main>
        <Footer /> 
      </div>
    </BrowserRouter>
  );
}