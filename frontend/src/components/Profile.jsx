import { useEffect, useState } from "react";
import { getProfile } from "../api/profile";
import ProfileButton from "./Header";

export default function Profile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    getProfile().then(setUser).catch(console.error);
  }, []);

  if (!user) return <p className="text-center mt-10">Загрузка...</p>;

  return (
    <div className="max-w-md mx-auto mt-10 bg-white shadow p-6 rounded-xl">
      <h1 className="text-2xl font-semibold mb-4">Личный кабинет</h1>
      <p><strong>Имя:</strong> {user.username}</p>
      <p><strong>Email:</strong> {user.email}</p>
      <p><strong>Телефон:</strong> {user.phone_number || "—"}</p>
    </div>
  );
}
