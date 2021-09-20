from sqlalchemy import Column, Integer, String


from db.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String, index=True)
    role = Column(String, index=True)


class Map(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String, index=True)


class Gamemode(Base):
    __tablename__ = "gamemodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String, index=True)
