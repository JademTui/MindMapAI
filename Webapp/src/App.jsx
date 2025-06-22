// 📁 webapp/src/App.jsx
import React from 'react'
import 'reactflow/dist/style.css'

import SystemStatusCard from './components/SystemStatusCard'
import MemoryChartCard from './components/MemoryChartCard'
import InteractionLogCard from './components/InteractionLogCard'
import ShadowControlPanel from './components/ShadowControlPanel'
import MemoryRoutingPanel from './components/MemoryRoutingPanel' // ✅ NEW
import ShadowTrainingPanel from './components/ShadowTrainingPanel' // ✅ NEW

export default function App() {
  return (
    <div className="h-screen w-screen flex flex-col bg-gray-50 overflow-hidden">
      <h1 className="text-3xl font-bold p-4 text-center">🧠 MindMapAI System Overview</h1>

      <div className="flex flex-row gap-4 px-6 h-full">
        {/* Left: Dynamic System Map */}
        <div className="flex-1">
          <DynamicMindMap />
        </div>

        {/* Right: Console + Stats Panel */}
        <div className="w-[360px] space-y-4 overflow-y-auto p-1">
          <SystemStatusCard />
          <MemoryChartCard />
          <InteractionLogCard />
          <ShadowControlPanel />
          <MemoryRoutingPanel />      {/* ✅ New Panel */}
          <ShadowTrainingPanel />     {/* ✅ New Panel */}
        </div>
      </div>
    </div>
  )
}
