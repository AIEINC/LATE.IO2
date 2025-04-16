from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import os, json, httpx

router = APIRouter()
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
DISCORD_REDIRECT_URI = os.getenv("DISCORD_REDIRECT_URI", "http://localhost:7860/auth/discord/callback")
auth_base = "https://discord.com/api/oauth2"

@router.get("/auth/discord")
async def discord_login():
    scopes = "identify email guilds.join"
    return RedirectResponse(
        url=f"{auth_base}/authorize?client_id={DISCORD_CLIENT_ID}&redirect_uri={DISCORD_REDIRECT_URI}&response_type=code&scope={scopes}"
    )

@router.get("/auth/discord/callback")
async def discord_callback(request: Request):
    code = request.query_params.get("code")
    token_url = f"{auth_base}/token"

    data = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": DISCORD_REDIRECT_URI,
        "scope": "identify email guilds.join"
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    async with httpx.AsyncClient() as client:
        resp = await client.post(token_url, data=data, headers=headers)
        token_data = resp.json()

    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}

    creds["discord"] = token_data
    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)

    return RedirectResponse(url="/frontend/index.html")