from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/lookup/wayback")
async def wayback_snapshots(url: str):
    api_url = f"http://archive.org/wayback/available?url={url}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(api_url)
        return resp.json()