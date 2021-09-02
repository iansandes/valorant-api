import requests

from os import name
from typing import List
from fastapi import Depends, FastAPI

import schemas

app = FastAPI()


@app.get("/agents/", response_model=List[schemas.Agent])
def get_agents():
    agents = []
    agents_return = requests.get("https://valorant-api.com/v1/agents/?language=pt-BR")
    agents_return = agents_return.json()
    for agent in agents_return["data"]:
        if agent["displayName"] == "Sova":
            new_agent = schemas.Agent(
                name=agent["displayName"],
                description=agent["description"],
                image=agent["displayIcon"],
                role="Iniciador",
            )
        else:
            new_agent = schemas.Agent(
                name=agent["displayName"],
                description=agent["description"],
                image=agent["displayIcon"],
                role=agent["role"]["displayName"],
            )
        agents.append(new_agent)
    return agents
