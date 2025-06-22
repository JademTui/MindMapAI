// 📁 webapp/src/components/NodeDetailModal.jsx
import React from 'react';

export default function NodeDetailModal({ node, onClose }) {
  if (!node) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-30 backdrop-blur-sm flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-xl shadow-xl max-w-md w-full">
        <h2 className="text-lg font-semibold mb-2">🔍 Node Detail</h2>
        <p className="mb-2"><strong>ID:</strong> {node.id}</p>
        <p className="mb-2"><strong>Label:</strong> {node.data?.label}</p>
        <p className="text-sm text-gray-500 mb-4">Position: ({node.position.x}, {node.position.y})</p>

        {/* Placeholder for future diagnostic data */}
        <div className="text-sm text-gray-600 border-t pt-2">
          <p>🧠 Live diagnostic snapshot could go here.</p>
        </div>

        <div className="text-right mt-4">
          <button onClick={onClose} className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
