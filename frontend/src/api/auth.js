export async function login(email, password) {
  const res = await fetch("http://localhost:8000/users/login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) throw new Error("Неверный email или пароль");
  const data = await res.json();
  localStorage.setItem("accessToken", data.access);
  localStorage.setItem("refreshToken", data.refresh);
  return data;
}

export async function refreshToken() {
  const refresh = localStorage.getItem("refreshToken");
  const res = await fetch("http://localhost:8000/token/refresh/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh }),
  });

  if (!res.ok) throw new Error("Не удалось обновить токен");
  const data = await res.json();
  localStorage.setItem("accessToken", data.access);
  return data.access;
}
