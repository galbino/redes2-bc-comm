from fastapi import APIRouter
from ..model import CommunicationResponse

router = APIRouter(prefix="/api/v1/comm", tags=["comm"])


@router.get("", summary="", response_model=CommunicationResponse, status_code=200, response_model_exclude_unset=True)
async def test():
    return "", 200
