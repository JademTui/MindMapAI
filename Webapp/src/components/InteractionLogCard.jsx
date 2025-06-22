// 📁 webapp/src/components/InteractionLogCard.jsx
import React, { useEffect, useState } from 'react'

export default function InteractionLogCard() {
  const [logs, setLogs] = useState([])

  useEffect(() => {
    fetch('/api/v1/system/status')
      .then(res => res.json())
      .then(data => {
        const recent = data.recent_activity || []
        const parsed = recent.map((entry, index) => {
          const parts = entry.split('\n')
          return { id: index, user: parts[0] || '', ai: parts[1] || '' }
        })
        setLogs(parsed)
      })
      .catch(err => console.error('Failed to fetch interaction logs:', err))
  }, [])

  return (
    <div className="bg-white border rounded-xl shadow p-4">
      <h3 className="text-lg font-semibold mb-2">💬 Recent Interactions</h3>
      <div className="space-y-3 text-sm text-gray-700 max-h-60 overflow-y-auto pr-2">
        {logs.length === 0 && <p className="text-gray-400">No recent interactions recorded.</p>}
        {logs.map(({ id, user, ai }) => (
          <div key={id} className="border-b pb-2">
            <p><strong>You:</strong> {user}</p>
            <p className="text-blue-700"><strong>AI:</strong> {ai}</p>
          </div>
        ))}
      </div>
    </div>
  )
}