// 📁 webapp/src/components/MemoryChartCard.jsx
import React, { useEffect, useState } from 'react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts'

export default function MemoryChartCard() {
  const [data, setData] = useState([])

  useEffect(() => {
    fetch("/api/v1/system/status")
      .then(res => res.json())
      .then(stats => {
        const breakdown = stats.module_breakdown || {}
        const chartData = Object.entries(breakdown).map(([source, count]) => ({ source, count }))
        setData(chartData)
      })
      .catch(err => {
        console.error("Chart data failed:", err)
      })
  }, [])

  return (
    <div className="bg-white border rounded-xl shadow p-4">
      <h3 className="text-lg font-semibold mb-2">📊 Memory Source Distribution</h3>
      <ResponsiveContainer width="100%" height={250}>
        <BarChart data={data} layout="vertical" margin={{ left: 20, bottom: 10 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" allowDecimals={false} hide />
          <YAxis type="category" dataKey="source" width={100} />
          <Tooltip />
          <Bar dataKey="count" fill="#3b82f6" radius={[0, 6, 6, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}