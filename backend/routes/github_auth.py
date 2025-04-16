from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
import os, json, httpx

router = APIRouter()
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI", "http://localhost:7860/auth/github/callback")

@router.get("/auth/github")
async def github_login():
    return RedirectResponse(
        url=f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=repo%20read:user"
    )

@router.get("/auth/github/callback")
async def github_callback(request: Request):
    code = request.query_params.get("code")

    async with httpx.AsyncClient() as client:
        resp = await client.post("https://github.com/login/oauth/access_token",
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": GITHUB_REDIRECT_URI
            },
            headers={"Accept": "application/json"}
        )
        token_data = resp.json()

    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}

    creds["github"] = token_data
    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)

    return RedirectResponse(url="/frontend/index.html")