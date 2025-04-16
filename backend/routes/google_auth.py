
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
import os, json

router = APIRouter()

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://oauth2.googleapis.com/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={
        'scope': 'openid email profile https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/documents https://www.googleapis.com/auth/calendar',
        'prompt': 'consent'
    }
)

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

@router.get("/auth/google")
async def login(request: Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/google/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    
    # Load or create credential store
    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}

    creds["google"] = token

    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)

    return RedirectResponse(url="/frontend/index.html")
