// 📁 webapp/src/components/MemoryRoutingPanel.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function MemoryRoutingPanel() {
  const [expanded, setExpanded] = useState(false);
  const [routes, setRoutes] = useState([]);
  const [filter, setFilter] = useState("all");

  useEffect(() => {
    if (expanded) {
      fetchRoutes();
      const interval = setInterval(fetchRoutes, 5000);
      return () => clearInterval(interval);
    }
  }, [expanded, filter]);

  const fetchRoutes = async () => {
    try {
      const res = await axios.get('/api/v1/routes?limit=20');
      const filtered = filter === "all" ? res.data : res.data.filter(r => r.source === filter);
      setRoutes(filtered);
    } catch (err) {
      console.error('Memory route fetch error:', err);
    }
  };

  return (
    <div className="bg-white border rounded-lg shadow p-4 mt-4">
      <button
        className="font-bold text-blue-600 hover:underline mb-2"
        onClick={() => setExpanded(!expanded)}
      >
        {expanded ? '🔽 Hide Memory Routing Log' : '▶️ Show Memory Routing Log'}
      </button>

      {expanded && (
        <div>
          <div className="mb-2">
            <label className="text-sm mr-2">Filter by Source:</label>
            <select value={filter} onChange={(e) => setFilter(e.target.value)} className="text-sm border rounded px-2 py-1">
              <option value="all">All</option>
              <option value="chat">Chat</option>
              <option value="shadow">Shadow</option>
              <option value="plugin">Plugin</option>
              <option value="deferred">Deferred</option>
            </select>
          </div>

          <div className="space-y-2 max-h-[300px] overflow-y-auto">
            {routes.length === 0 ? (
              <p className="text-sm text-gray-500">No recent routes found.</p>
            ) : (
              routes.map((log, idx) => (
                <div key={idx} className="border-b pb-2 text-sm">
                  <div>🧠 <strong>{log.type}</strong> from <span className="italic">{log.source}</span></div>
                  <div className="text-gray-500">Args: {JSON.stringify(log.args)}</div>
                  <div className="text-xs text-gray-400">{log.timestamp}</div>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
}
