---
title: LATE.IO2
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
sdk_version: "1.0"
app_file: backend/app.py
pinned: false
---



# Agentic Terraforming

Agentic Terraforming is a modular, memory-driven AI framework designed to simulate intelligent agent behavior using document digestion, feedback loops, and real-world integration.

---

## Features

### DIGS (Digestive Information Grouping System)
- Segments documents into 2,000-character blocks
- Runs 8-path analysis (summary, concept, terms, structure, data, comparison, application, cross-ref)
- Outputs indexed memory for agents to recall and evolve from

### Modular Button Architecture (18 Panels)
- Button 01: Upload DIGS or agent behaviors
- Button 02: Run simulation and generate sandbox
- Button 03: DIGS analysis viewer
- Button 04: Mind map brain UI
- Button 05–17: Memory tools, task queues, feedback, OAuth, logging, admin, and more
- Button 18: Full configuration settings with JSON sync

### OAuth Integration
- Live credential console
- Dynamic service tokenization
- Visual status map for all connected services

### Agent Profiles & Feedback Loops
- Customizable agent memory and traits
- Reinforcement-style feedback tracking
- Segment-level journaling, historical logs, and audit trail

---

## File Structure

```
/backend/               - Flask routes and memory engines
/frontend/              - index.html, templates, visual panels
/data/                  - Agent logs, memory segments, uploads
/docs/                  - System map and install guide
system_settings.json    - Editable config (panel 18)
requirements.txt        - Python dependencies
Dockerfile              - Containerized deployment
```

---

## How to Run (Local)

```bash
# Clone repo
git clone https://codeberg.org/YOUR_USERNAME/agentic_terraforming.git
cd agentic_terraforming

# Setup environment
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Start backend
python backend/app.py
```

---

## License

MIT — use, remix, extend, and terraform freely.
=======
# Agentic Terraforming System

This is the official deployment of the **Late Liquidity Agentic Terraforming Environment** — an advanced AI system integrating cognitive dataflow, spreadsheet memory mapping, agentic behavior, and multiplexed logic visualization.

## Features

- Dynamic spreadsheet-driven memory simulation
- Modular agent system with pluggable logic layers
- OAuth-based integration with Google, Notion, Reddit, Discord, GitHub, Hugging Face, and more
- DIGS (Digestive Information Grouping System) for long-term memory structuring
- Real-time mindmap-based UI
- Streamlit frontend powered by neural simulation models

## How to Use

1. Upload your CSV or connect a data stream.
2. Agents will auto-generate based on neuro-segment traits.
3. Use the interactive interface to visualize agent activity, relationships, and memory state.
4. Connect external services securely via in-app OAuth prompts.

## License

This project is available under a custom license. Commercial or derivative use must be pre-approved. Contact: **aiecangrow@gmail.com**

© Joseph Andre Yves Lacroix
