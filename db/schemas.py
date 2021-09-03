from pydantic import BaseModel


class Agent(BaseModel):

    name: str
    description: str
    image: str
    role: str

    class Config:
        orm_mode = True
