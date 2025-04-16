
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import os, json, urllib.parse
import httpx

router = APIRouter()

NOTION_CLIENT_ID = os.getenv("NOTION_CLIENT_ID")
NOTION_CLIENT_SECRET = os.getenv("NOTION_CLIENT_SECRET")
NOTION_REDIRECT_URI = os.getenv("NOTION_REDIRECT_URI", "http://localhost:7860/auth/notion/callback")
NOTION_TOKEN_URL = "https://api.notion.com/v1/oauth/token"
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

@router.get("/auth/notion")
async def auth_notion():
    query = urllib.parse.urlencode({
        "client_id": NOTION_CLIENT_ID,
        "response_type": "code",
        "owner": "user",
        "redirect_uri": NOTION_REDIRECT_URI
    })
    return RedirectResponse(url=f"https://api.notion.com/v1/oauth/authorize?{query}")

@router.get("/auth/notion/callback")
async def auth_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "No code returned from Notion."}

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            NOTION_TOKEN_URL,
            auth=(NOTION_CLIENT_ID, NOTION_CLIENT_SECRET),
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": NOTION_REDIRECT_URI
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        token_data = resp.json()

    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}

    creds["notion"] = token_data

    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)

    return RedirectResponse(url="/frontend/index.html")
