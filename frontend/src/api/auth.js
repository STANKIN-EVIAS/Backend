import { API_URL } from "./config";

export async function login(email, password) {
  const res = await fetch(`${API_URL}/auth/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  console.log(res)
  if (!res.ok) throw new Error("Неверный email или пароль");
  const data = await res.json();
  localStorage.setItem("accessToken", data.access);
  localStorage.setItem("refreshToken", data.refresh);
  return data;
}

export async function refreshToken() {
  const refresh = localStorage.getItem("refreshToken");
  const res = await fetch(`${API_URL}/auth/token/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh }),
  });

  if (!res.ok) throw new Error("Не удалось обновить токен");
  const data = await res.json();
  localStorage.setItem("accessToken", data.access);
  return data.access;
}

export async function logout() {
  // Удаляем токены из localStorage
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  
  // Здесь можно добавить запрос к API для инвалидации токена на сервере
  try {
    const token = localStorage.getItem("accessToken");
    if (token) {
      await fetch(`${API_URL}/auth/logout/`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        }
      });
    }
  } catch (error) {
    console.error("Ошибка при выходе:", error);
  }
}
