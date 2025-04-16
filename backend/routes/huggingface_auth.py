from fastapi import APIRouter
import os, json

router = APIRouter()
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "../data/user_credentials.json")

@router.post("/auth/huggingface")
def store_hf_pat(token: str):
    try:
        with open(CREDENTIALS_PATH, "r") as f:
            creds = json.load(f)
    except:
        creds = {}
    creds["huggingface"] = {"token": token}
    with open(CREDENTIALS_PATH, "w") as f:
        json.dump(creds, f)
    return {"message": "Hugging Face token saved."}