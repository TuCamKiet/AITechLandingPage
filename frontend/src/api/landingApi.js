import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export const getLandingData = async () => {
  const response = await api.get("/landing");
  console.log("front", response.data);
  return response.data;
};
