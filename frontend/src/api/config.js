export const API_URL = process.env.REACT_APP_BACKEND_API_URL;


if (!API_URL) {
  console.error("❌ REACT_APP_BACKEND_API_URL не определён в .env!");
}
else {
    console.log(API_URL)
}