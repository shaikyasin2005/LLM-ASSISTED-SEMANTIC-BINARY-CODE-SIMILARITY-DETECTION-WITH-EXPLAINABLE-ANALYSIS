import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
});

export const compareCodes = (code1, code2) =>
  API.post("/similarity/compare", null, {
    params: { code1, code2 }
  });

export const aiExplain = (code1, code2) =>
  API.post("/explain/ai", null, {
    params: { code1, code2 }
  });