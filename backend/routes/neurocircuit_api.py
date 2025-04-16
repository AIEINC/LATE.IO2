from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()
CIRCUIT_PATH = os.path.join(os.path.dirname(__file__), "../data/neurocircuit_board.csv")

@router.get("/api/agents/neurocircuit")
def get_neurocircuit_agents():
    if not os.path.exists(CIRCUIT_PATH):
        return {"agents": []}
    df = pd.read_csv(CIRCUIT_PATH)
    agents = df.to_dict(orient="records")
    return {"agents": agents}