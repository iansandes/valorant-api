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
