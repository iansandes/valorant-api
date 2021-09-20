from db import models, schemas
from sqlalchemy.orm import Session


def get_agents(db: Session):
    return db.query(models.Agent).all()


def get_agent(db: Session, agent_name: str):
    return (
        db.query(models.Agent).filter(models.Agent.name == agent_name).first()
    )  # noqa


def create_agent(db: Session, agent: schemas.Agent):
    db_agent = models.Agent(
        name=agent.name,
        description=agent.description,
        image=agent.image,
        role=agent.role,
    )
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)


def get_maps(db: Session):
    return db.query(models.Map).all()


def get_map(db: Session, map_name: str):
    return db.query(models.Map).filter(models.Map.name == map_name).first()  # noqa


def create_map(db: Session, map: schemas.Map):
    db_map = models.Map(
        name=map.name,
        image=map.image,
    )
    db.add(db_map)
    db.commit()
    db.refresh(db_map)


def get_gamemodes(db: Session):
    return db.query(models.Gamemode).all()


def get_gamemode(db: Session, gamemode_name: str):
    return (
        db.query(models.Gamemode)
        .filter(models.Gamemode.name == gamemode_name)
        .first()  # noqa
    )


def create_gamemode(db: Session, gamemode: schemas.Gamemode):
    db_gamemode = models.Gamemode(
        name=gamemode.name,
        image=gamemode.image,
    )
    db.add(db_gamemode)
    db.commit()
    db.refresh(db_gamemode)
