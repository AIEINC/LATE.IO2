from fastapi import APIRouter, Query
import httpx

router = APIRouter()

@router.get("/search/dork")
async def google_dork(q: str = Query(...)):
    search_url = f"https://www.google.com/search?q={q}"
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(search_url, headers=headers)
        return {"status": resp.status_code, "raw_html": resp.text[:1000]}