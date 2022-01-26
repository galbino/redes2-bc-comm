from pydantic import BaseModel, Field
from typing import Optional, List


class BlockData(BaseModel):
    sender: str
    receiver: str
    amount: int


class BlockDataOptional(BaseModel):
    sender: str
    receiver: Optional[str]
    amount: int


class BlockResponse(BaseModel):
    index: int
    previous_hash: str = Field(alias="previousHash")
    data: BlockDataOptional
    hash: str
    difficulty: int
    timestamp: str


class GetUserBlocks(BaseModel):
    envio: List[BlockResponse] = Field(alias="sent")
    recebido: List[BlockResponse] = Field(alias="received")

    class Config:
        allow_population_by_field_name = True
