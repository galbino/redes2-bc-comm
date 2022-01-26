from fastapi import APIRouter
from ..model import BlockData, BlockResponse, GetUserBlocks
from ..services.block_service import BlockService

router = APIRouter(prefix="/api/v1/block", tags=["block"])


@router.post("", summary="Add a new block to the chain.", response_model=BlockResponse, status_code=200, response_model_exclude_unset=True)
async def add_new_block(comm_data: BlockData):
    comm_service = BlockService()
    resp = await comm_service.add_new_block(comm_data)
    return resp


@router.get("/check", summary="Check blocks integrity.", status_code=200, response_model_exclude_unset=True)
async def check_block_integrity():
    comm_service = BlockService()
    resp = await comm_service.check_integrity()
    data = {"intact": resp}
    return data


@router.get("/user/{user_id}", response_model=GetUserBlocks, summary="Get all transactions related to an user, both receiving and sending.", status_code=200, response_model_exclude_unset=True)
async def get_blocks_by_user(user_id: str):
    comm_service = BlockService()
    resp = await comm_service.get_blocks_by_user(user_id)
    return resp

