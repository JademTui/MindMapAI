// 📁 webapp/src/components/SystemStatusCard.jsx
import { useEffect, useState } from 'react';

export default function SystemStatusCard() {
  const [status, setStatus] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/v1/system/status")
      .then((res) => res.json())
      .then((data) => setStatus(data))
      .catch((err) => setError(err.message));
  }, []);

  if (error) {
    return (
      <div className="p-4 bg-red-100 text-red-800 rounded-xl shadow">
        <p>❌ Error: {error}</p>
      </div>
    );
  }

  if (!status) {
    return (
      <div className="p-4 bg-gray-100 text-gray-600 rounded-xl animate-pulse">
        <p>Loading system status...</p>
      </div>
    );
  }

  return (
    <div className="p-6 bg-white border rounded-2xl shadow-xl">
      <h2 className="text-xl font-semibold mb-2">🧠 System Health</h2>
      <p className="text-sm text-gray-600 mb-1">⏱ {status.timestamp}</p>
      <p className="text-green-700 font-medium">{status.status}</p>
      <div className="mt-3 space-y-1 text-sm">
        <p>📊 Alignment Score: <strong>{status.alignment_score.toFixed(2)}</strong></p>
        <p>🧠 Memory Entries: {status.memory_entries}</p>
        <p>📂 Sources: {Object.entries(status.module_breakdown || {}).map(([k, v]) => `${k}: ${v}`).join(", ")}</p>
      </div>
      {status.recent_activity && (
        <div className="mt-3 text-xs text-gray-500">
          <p>🕒 Recent Activity:</p>
          <ul className="list-disc ml-4">
            {status.recent_activity.map((item, i) => (
              <li key={i}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
