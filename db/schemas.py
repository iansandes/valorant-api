from pydantic import BaseModel


class Agent(BaseModel):

    id: int
    name: str
    description: str
    image: str
    role: str

    class Config:
        orm_mode = True
