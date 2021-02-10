from typing import Optional

from fastapi import FastAPI, HTTPException

from table_manager import TableManager
from entity_manager import EntityManger
from client_factory import ClientFactory

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tables")
def create_table(table_name: str):
    client = ClientFactory.getTableServiceClient()
    result = TableManager.create_table(client, table_name)
    if not result:
        raise HTTPException(status_code=400, detail='Table already exists.')


@app.post("/entities")
def create_entity(table_name: str):
    client = ClientFactory.getTableClient(table_name)
    result = EntityManger.create_entity(client)
    if not result:
        raise HTTPException(status_code=400, detail='Entity already exists.')


@app.delete("/entities")
def delete_entity(table_name: str):
    client = ClientFactory.getTableClient(table_name)
    result = EntityManger.delete_entity(client)
    raise HTTPException(status_code=400, detail='Entity does not exist.')


@app.delete("/tables")
def delete_table(table_name: str):
    client = ClientFactory.getTableServiceClient()
    result = TableManager.delete_table(client, table_name)
    if not result:
        raise HTTPException(status_code=400, detail='Table does not exist.')
