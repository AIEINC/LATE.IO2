from fastapi import APIRouter, UploadFile, File
from backend.routes.generate_segment_trait_mappings import process_traits
import tempfile
import shutil
import os

router = APIRouter()

@router.post("/upload-digs-csv/")
async def upload_digs_csv(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        result = process_traits(tmp_path)
        os.unlink(tmp_path)
        return {"success": True, "mappings": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
