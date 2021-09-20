import requests

from typing import List
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


from db import models, repository, schemas
from db.database import SessionLocal, engine

from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/agents/", response_model=List[schemas.Agent])
def get_agents(db: Session = Depends(get_db)):
    agents = repository.get_agents(db)
    return agents


@app.get("/sync_agents/")
def sync_agents(db: Session = Depends(get_db)):
    agents_return = requests.get(
        "https://valorant-api.com/v1/agents?isPlayableCharacter=true&language=pt-BR"  # noqa
    )
    agents_return = agents_return.json()
    for agent in agents_return["data"]:
        new_agent = models.Agent(
            name=agent["displayName"],
            description=agent["description"],
            image=agent["fullPortrait"],
            role=agent["role"]["displayName"],
        )
        db_agent = repository.get_agent(db, new_agent.name)
        if db_agent:
            continue
        repository.create_agent(db=db, agent=new_agent)

    return {"message": "Agents was sync!"}


@app.get("/maps/", response_model=List[schemas.Map])
def get_maps(db: Session = Depends(get_db)):
    maps = repository.get_maps(db)
    return maps


@app.get("/sync_maps/")
def sync_maps(db: Session = Depends(get_db)):
    maps_return = requests.get(
        "https://valorant-api.com/v1/maps/?language=pt-BR"
    )  # noqa
    maps_return = maps_return.json()
    for map in maps_return["data"]:
        new_map = schemas.Map(
            name=map["displayName"],
            image=map["splash"],
        )
        db_map = repository.get_map(db, new_map.name)
        if db_map:
            continue
        repository.create_map(db=db, map=new_map)

    return {"message": "Maps was sync!"}
