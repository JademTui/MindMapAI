// 📁 webapp/src/components/ShadowControlPanel.jsx
import React from 'react'

export default function ShadowControlPanel() {
  const triggerAction = async (action) => {
    try {
      const res = await fetch(`/api/v1/system/${action}`)
      const result = await res.json()
      alert(`✅ ${action} success:\n` + (result?.message || JSON.stringify(result)))
    } catch (err) {
      console.error(err)
      alert(`❌ ${action} failed.`)
    }
  }

  return (
    <div className="bg-white border rounded-xl shadow p-4 space-y-3">
      <h3 className="text-lg font-semibold">🛠️ ShadowNet Control</h3>
      <div className="grid grid-cols-1 gap-2">
        <button onClick={() => triggerAction('train')} className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
          🧬 Train ShadowNet Now
        </button>
        <button onClick={() => triggerAction('reflect')} className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700">
          🔁 Reflect on Memory
        </button>
        <button onClick={() => triggerAction('wipe')} className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700">
          🧹 Reset Shadow Memory
        </button>
      </div>
    </div>
  )
}
