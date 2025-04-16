import React, { useEffect, useState } from 'react';
import './visualizer.css';

export default function AgentVisualizer() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    fetch('/api/agents/neurocircuit')
      .then(res => res.json())
      .then(data => setAgents(data.agents || []));
  }, []);

  return (
    <div className="agent-visualizer">
      <h2>Agent Network Grid</h2>
      <div className="grid">
        {agents.map((agent, index) => (
          <div key={index} className="agent-card">
            <div className="triangle">
              <div className="vertex function">{agent.function}</div>
              <div className="vertex communication">{agent.communication}</div>
              <div className="vertex security">{agent.security}</div>
            </div>
            <div className="meta">
              <p>ID: {agent.id}</p>
              <p>Entropy: {agent.entropy}</p>
              <p>Tier: {agent.tier}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}