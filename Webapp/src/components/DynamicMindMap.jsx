// 📁 webapp/src/components/DynamicMindMap.jsx
import React, { useEffect, useState } from 'react'
import ReactFlow, { Background, Controls } from 'reactflow'
import 'reactflow/dist/style.css'
import NodeDetailModal from './NodeDetailModal'

export default function DynamicMindMap() {
  const [nodes, setNodes] = useState([])
  const [edges, setEdges] = useState([])
  const [activeNode, setActiveNode] = useState(null)

  useEffect(() => {
    fetch("/api/v1/system/status")
      .then(res => res.json())
      .then(data => {
        const score = data.alignment_score?.toFixed(2) || "0.00"
        const mem = data.memory_entries || 0

        const newNodes = [
          { id: '1', position: { x: 100, y: 100 }, data: { label: '🧠 AI Core' }, type: 'input' },
          { id: '2', position: { x: 400, y: 100 }, data: { label: `🧬 ShadowNet\nScore: ${score}` } },
          { id: '3', position: { x: 250, y: 250 }, data: { label: `📚 Memory\nEntries: ${mem}` } },
        ]

        const newEdges = [
          { id: 'e1-2', source: '1', target: '2', animated: true },
          { id: 'e2-3', source: '2', target: '3', animated: true },
          { id: 'e1-3', source: '1', target: '3' },
        ]

        setNodes(newNodes)
        setEdges(newEdges)
      })
      .catch(err => {
        console.error("Error loading map:", err)
        setNodes([{
          id: 'fail', position: { x: 150, y: 150 }, data: { label: '❌ Failed to load map' }
        }])
        setEdges([])
      })
  }, [])

  const handleNodeClick = (_, node) => {
    setActiveNode(node)
  }

  return (
    <div className="h-[600px] border rounded-xl shadow bg-white relative">
      <ReactFlow nodes={nodes} edges={edges} onNodeClick={handleNodeClick} fitView>
        <Background />
        <Controls />
      </ReactFlow>
      <NodeDetailModal node={activeNode} onClose={() => setActiveNode(null)} />
    </div>
  )
}
