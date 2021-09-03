from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from db.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)
    role = Column(String, index=True)
