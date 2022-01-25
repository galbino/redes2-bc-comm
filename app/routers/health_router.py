from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/check")


@router.get("/", include_in_schema=False)
async def check():
    return PlainTextResponse("ok", status_code=200)
