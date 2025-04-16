from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/neurocircuit_board.csv")

@router.get("/api/agents/mindmap")
def get_agent_mindmap():
    if not os.path.exists(DATA_PATH):
        return {"name": "Agentic Core", "children": []}

    df = pd.read_csv(DATA_PATH)
    children = []
    for _, row in df.iterrows():
        children.append({
            "name": row.get("AgentID", "Unknown Agent"),
            "tier": row.get("Tier", "Unknown"),
            "entropy": row.get("Entropy", 0)
        })

    return {"name": "Agentic Core", "children": children}