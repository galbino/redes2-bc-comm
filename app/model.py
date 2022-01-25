from pydantic import BaseModel


class CommunicationResponse(BaseModel):
    sender: str
    receiver: str
    amount: str
