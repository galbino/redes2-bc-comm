from ext import settings
import aiohttp
from ..model import BlockData


class BlockService:
    def __init__(self):
        self.base_url = settings.dict().get("BASE_URL")

    async def add_new_block(self, body_model: BlockData) -> dict:
        body = body_model.dict(by_alias=True)
        async with aiohttp.ClientSession() as session:
            req_resp = await session.post(f"{self.base_url}/addblock", json=body)
            json_data = await req_resp.json()
        return json_data

    async def check_integrity(self) -> bool:
        async with aiohttp.ClientSession() as session:
            req_resp = await session.get(f"{self.base_url}/check")
            json_data = await req_resp.json()
        return json_data

    async def get_blocks_by_user(self, sender: str) -> dict:
        body = {
            "user": sender
        }
        async with aiohttp.ClientSession() as session:
            req_resp = await session.post(f"{self.base_url}/filter", json=body)
            json_data = await req_resp.json()
        return json_data
