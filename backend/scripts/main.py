from fastapi import FastAPI, HTTPException
app = FastAPI()

LICENSE_KEYS = {
    "abc-basic": "basic",
    "xyz-pro": "pro",
    "ent-999": "enterprise"
}

@app.post("/validate")
def validate_license(data: dict):
    key = data.get("key")
    if key not in LICENSE_KEYS:
        raise HTTPException(status_code=403, detail="Invalid license key")
    return {"tier": LICENSE_KEYS[key]}
