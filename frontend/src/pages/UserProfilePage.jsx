import { useEffect, useState } from "react";
import { getProfile } from "../api/profile";

export default function Profile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    getProfile().then(setUser).catch(console.error);
  }, []);

  if (!user) return <p className="text-center mt-10">Загрузка...</p>;
  
  return (
    <div className="max-w-md mx-auto mt-10 bg-white shadow p-6 rounded-xl">
        <div className="flex items-center gap-4 mb-6">
            <img
            src={user.image}
            alt="Аватар пользователя"
            className="w-16 h-16 rounded-full object-cover border"
            />
            <div>
            <h1 className="text-2xl font-semibold">{user.username}</h1>
            <p className="text-gray-500">{user.email}</p>
            </div>
        </div>

        <div className="border-t pt-4">
            <h2 className="text-xl font-semibold mb-2">Мои питомцы</h2>

            {user.pets && user.pets.length > 0 ? (
            <ul className="space-y-3">
                {user.pets.map((pet) => (
                <li
                    key={pet.id}
                    className="flex items-center gap-4 bg-gray-50 p-3 rounded-lg"
                >
                    <img
                    src={pet.image}
                    alt={pet.name}
                    className="w-14 h-14 object-cover rounded-full border"
                    />
                    <div>
                    <p className="font-semibold">{pet.name}</p>
                    <p className="text-sm text-gray-600">{pet.species}</p>
                    <p className="text-sm text-gray-500">
                        {pet.genus}, {pet.gender}
                    </p>
                    </div>
                </li>
                ))}
            </ul>
            ) : (
            <p className="text-gray-500">У вас пока нет питомцев</p>
            )}
        </div>
    </div>


  );
}
