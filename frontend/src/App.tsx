import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const API_BASE = "http://127.0.0.1:8000/api";

interface Config {
  max_len: number;
  thickness: number;
  width: number;
  margin: number;
  rpm: number;
}

function App() {
  const [status, setStatus] = useState({ meters: 0, rpm: 0, is_winding: false, is_parking: false });
  const [config, setConfig] = useState<Config>({ max_len: 100, thickness: 1.75, width: 200, margin: 10, rpm: 50 });
  const [selectedParam, setSelectedParam] = useState<keyof Config>('max_len');
  const [step, setStep] = useState(1);
  const [connected, setConnected] = useState(false);

  // СТАН ДЛЯ ALERT ВІКНА
  const [alertConfig, setAlertConfig] = useState({
    isOpen: false,
    message: '',
    onConfirm: () => {},
  });

  useEffect(() => {
    const fetchAll = async () => {
      try {
        const res = await axios.get(`${API_BASE}/status`);
        if (res.data) setStatus(res.data);
        setConnected(true);
      } catch (e) { setConnected(false); }
    };
    const timer = setInterval(fetchAll, 500);
    return () => clearInterval(timer);
  }, []);

  const adjustValue = (dir: number) => {
    setConfig(prev => {
      let newValue = prev[selectedParam] + (dir * step);
      newValue = Math.max(0, newValue);
      newValue = Number(newValue.toFixed(2));
      return { ...prev, [selectedParam]: newValue };
    });
  };

  // ФУНКЦІЯ ВИКЛИКУ ALERT ВІКНА
  const triggerAlert = (message: string, confirmAction: () => void) => {
    setAlertConfig({
      isOpen: true,
      message: message,
      onConfirm: confirmAction
    });
  };

  const closeAlert = () => {
    setAlertConfig(prev => ({ ...prev, isOpen: false }));
  };

  // Приклад: Дія для скидання метрів
  const handleResetMeters = () => {
    triggerAlert("Скинути фактичні метри на нуль?", async () => {
      // Тут запит до бекенду на скидання
      await axios.post(`${API_BASE}/reset`);
      closeAlert();
    });
  };

  return (
    <div className="qt-window">
      {/* --- АЛЕРТ (ВСПЛИВАЮЧЕ ВІКНО) --- */}
      {alertConfig.isOpen && (
        <div className="alert-overlay">
          <div className="alert-box">
            <div className="alert-message">{alertConfig.message}</div>
            <div className="alert-buttons">
              <button className="alert-btn btn-cancel" onClick={closeAlert}>ВІДМІНА</button>
              <button className="alert-btn btn-ok" onClick={() => { alertConfig.onConfirm(); closeAlert(); }}>ОК</button>
            </div>
          </div>
        </div>
      )}

      {/* ЛІВА ЧАСТИНА */}
      <div className="left-displays">
        <div className="display-group">
          <label className="qt-label">Фактичні (М)</label>
          <div className="qt-lcd green-lcd">{(status?.meters || 0).toFixed(2)}</div>
        </div>
        <div className="display-group">
          <label className="qt-label">Об/Хв</label>
          <div className="qt-lcd">{(status?.rpm || 0).toFixed(1)}</div>
        </div>
        <div className={`conn-status ${connected ? 'online' : 'offline'}`}>
          {connected ? "СИСТЕМА ОНЛАЙН" : "ОЧІКУВАННЯ ДАНИХ..."}
        </div>
      </div>

      {/* ПРАВА ЧАСТИНА */}
      <div className="right-controls">
        <div className="params-grid">
          <button className={`param-btn ${selectedParam === 'max_len' ? 'active' : ''}`} onClick={() => setSelectedParam('max_len')}>
            <span className="p-title">Задано м</span>
            <span className="p-val">{config.max_len}</span>
          </button>
          <button className={`param-btn ${selectedParam === 'thickness' ? 'active' : ''}`} onClick={() => setSelectedParam('thickness')}>
            <span className="p-title">Діаметр мм</span>
            <span className="p-val">{config.thickness}</span>
          </button>
          <button className={`param-btn ${selectedParam === 'width' ? 'active' : ''}`} onClick={() => setSelectedParam('width')}>
            <span className="p-title">Ширина мм</span>
            <span className="p-val">{config.width}</span>
          </button>
          <button className={`param-btn ${selectedParam === 'margin' ? 'active' : ''}`} onClick={() => setSelectedParam('margin')}>
            <span className="p-title">Відступ мм</span>
            <span className="p-val">{config.margin}</span>
          </button>
          <button className={`param-btn wide-btn ${selectedParam === 'rpm' ? 'active' : ''}`} onClick={() => setSelectedParam('rpm')}>
            <span className="p-title">Об/Хв (Задано)</span>
            <span className="p-val">{config.rpm}</span>
          </button>
        </div>

        <div className="step-buttons">
          {[10, 1, 0.1, 0.01].map(s => (
            <button key={s} className={`step-btn ${step === s ? 'active' : ''}`} onClick={() => setStep(s)}>{s}</button>
          ))}
          {/* КНОПКА СКИДАННЯ ТЕПЕР ВИКЛИКАЄ АЛЕРТ */}
          <button className="reset-btn" onClick={handleResetMeters}>RESET</button>
        </div>

        <div className="action-row">
          <button className="math-btn" onClick={() => adjustValue(-1)}>-</button>
          <button className="math-btn" onClick={() => adjustValue(1)}>+</button>
          <button className="park-btn" onClick={() => {
            triggerAlert("Бажаєте запаркувати каретку?", () => axios.post(`${API_BASE}/park`))
          }}>ПАРК</button>
        </div>

        <div className="main-actions">
          <button
            className={`big-action-btn ${status.is_winding ? 'stop-btn' : 'start-btn'}`}
            onClick={() => axios.post(`${API_BASE}/${status.is_winding ? 'stop' : 'start'}`)}
            disabled={!connected}
          >
            {status.is_winding ? "СТОП" : "СТАРТ"}
          </button>
        </div>
      </div>
    </div>
  )
}

export default App