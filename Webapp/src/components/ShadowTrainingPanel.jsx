// 📁 webapp/src/components/ShadowTrainingPanel.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function ShadowTrainingPanel() {
  const [expanded, setExpanded] = useState(false);
  const [scores, setScores] = useState([]);
  const [reflection, setReflection] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchScores = async () => {
    try {
      const res = await axios.get('/api/v1/shadow/score-log');
      setScores(res.data);
    } catch (err) {
      console.error('Failed to fetch scores:', err);
    }
  };

  const fetchReflection = async () => {
    try {
      const res = await axios.get('/api/v1/shadow/last_reflection');
      setReflection(res.data.reflection);
    } catch (err) {
      console.error('Failed to fetch reflection:', err);
    }
  };

  const triggerTrain = async () => {
    setLoading(true);
    try {
      await axios.post('/api/v1/shadow/train');
      fetchScores();
      fetchReflection();
    } catch (err) {
      console.error('Training failed:', err);
    }
    setLoading(false);
  };

  useEffect(() => {
    if (expanded) {
      fetchScores();
      fetchReflection();
    }
  }, [expanded]);

  return (
    <div className="bg-white border rounded-lg shadow p-4 mt-4">
      <button
        className="font-bold text-purple-600 hover:underline mb-2"
        onClick={() => setExpanded(!expanded)}
      >
        {expanded ? '🔽 Hide Shadow Training Panel' : '▶️ Show Shadow Training Panel'}
      </button>

      {expanded && (
        <div className="space-y-4">
          <button
            onClick={triggerTrain}
            className="bg-purple-500 text-white px-4 py-1 rounded hover:bg-purple-600"
            disabled={loading}
          >
            {loading ? 'Training...' : 'Trigger ShadowNet Training'}
          </button>

          <div>
            <h3 className="font-semibold">🧠 Last Reflection</h3>
            <p className="text-sm text-gray-700 italic">{reflection}</p>
          </div>

          <div>
            <h3 className="font-semibold">📊 Alignment Scores</h3>
            <ul className="text-sm text-gray-600 space-y-1 max-h-[200px] overflow-y-auto">
              {scores.map((s, i) => (
                <li key={i}>Prompt: {s.prompt} → Score: {s.score.toFixed(3)}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}