import { refreshToken } from "./auth";

export async function getProfile() {
  let token = localStorage.getItem("accessToken");

  const res = await fetch("http://localhost:8000/users/profile/", {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });

  if (res.status === 401) {
    await refreshToken();
    return getProfile();
  }

  return res.json();
}
