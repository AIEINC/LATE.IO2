from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
import json

# Router imports
from backend.routes.discord_auth import router as discord_router
from backend.routes.dork_search import router as dork_router
from backend.routes.exploitdb_lookup import router as exploitdb_router
from backend.routes.github_auth import router as github_router
from backend.routes.google_auth import router as google_router
from backend.routes.huggingface_auth import router as hf_router
from backend.routes.mindmap_api import router as mindmap_router
from backend.routes.neurocircuit_api import router as neurocircuit_router
from backend.routes.notion_auth import router as notion_router
from backend.routes.reddit_auth import router as reddit_router
from backend.routes.spreadsheet_intake import router as spreadsheet_router
from backend.routes.wayback_lookup import router as wayback_router

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(discord_router)
app.include_router(dork_router)
app.include_router(exploitdb_router)
app.include_router(github_router)
app.include_router(google_router)
app.include_router(hf_router)
app.include_router(mindmap_router)
app.include_router(neurocircuit_router)
app.include_router(notion_router)
app.include_router(reddit_router)
app.include_router(spreadsheet_router)
app.include_router(wayback_router)

# Paths to CSVs for internal simulation
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
AGENTS_FILE = os.path.join(DATA_DIR, "Agentic_Deployment_Master_Plan_v3.2.csv")
DIGS_FILE = os.path.join(DATA_DIR, "DIGS_Cognitive_Psychology_Final_Output.csv")
MATRIX_FILE = os.path.join(DATA_DIR, "matrix.csv")

class SimulationInput(BaseModel):
    asset: str
    capital: float
    risk: int

@app.post("/simulate")
def simulate(input: SimulationInput):
    try:
        # Mock simulation logic placeholder
        result = {
            "yield": input.capital * (input.risk / 10),
            "notes": "Simulated outcome"
        }
        return {"projected_yield": result["yield"], "agent_notes": result.get("notes", "")}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def read_root():
    return {"message": "Server is running"}

@app.get("/agent_status")
def agent_status():
    try:
        df = pd.read_csv(AGENTS_FILE)
        enriched_agents = []
        for idx, row in df.iterrows():
            enriched_agents.append({
                "id": f"agent{idx}",
                "name": row.get("name", f"Agent {idx}"),
                "traits": row.get("traits", "unspecified"),
                "risk": int(row.get("risk", 3)),
                "status": "active",
                "memory_kb": 0,
                "endpoints": ["Google", "Notion", "Shodan"]
            })
        return {"active_agents": len(enriched_agents), "agents": enriched_agents}
    except Exception as e:
        return {"error": str(e)}
