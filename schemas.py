from pydantic import BaseModel

class Item(BaseModel):
    service: str
    data: str
