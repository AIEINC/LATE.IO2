from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import os, json, httpx, urllib.parse

router = APIRouter()
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDDIT_REDIRECT_URI", "http://localhost:7860/auth/reddit/callback")

@router.get("/auth/reddit")
async def reddit_login():
    state = "agentix_reddit"
    query = urllib.parse.urlencode({
        "client_id": CLIENT_ID,
        "response_type": "code",
        "state": state,
        "redirect_uri": REDIRECT_URI,
        "duration": "permanent",
        "scope": "identity read submit vote"
    })
    return RedirectResponse(url=f"https://www.reddit.com/api/v1/authorize?{query}")

@router.get("/auth/reddit/callback")
async def reddit_callback(request: Request):
    code = request.query_params.get("code")
    async with httpx.AsyncClient() as client:
        auth = httpx.BasicAuth(CLIENT_ID, CLIENT_SECRET)
        headers = {"User-Agent": "agentix/0.1"}
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI
        }
        response = await client.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
        token_data = response.json()

    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}

    creds["reddit"] = token_data
    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)

    return RedirectResponse(url="/frontend/index.html")