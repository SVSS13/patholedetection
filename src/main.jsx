import 'leaflet/dist/leaflet.css';

import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import { registerSW } from "virtual:pwa-register";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Addnearby from './Addnearby.jsx';

registerSW({ immediate: true });

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/nearby" element={<Addnearby />} />
    </Routes>

  </BrowserRouter>
);