from pydantic import BaseModel

class Item(BaseModel):
    service: str
    data: str

class MyserviceDB(BaseModel):
    current_id: int
