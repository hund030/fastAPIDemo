from typing import Optional

from fastapi import FastAPI, HTTPException

from table_manager import TableManager
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


@app.delete("/tables")
def delete_table(table_name: str):
    client = ClientFactory.getTableServiceClient()
    result = TableManager.delete_table(client, table_name)
    if not result:
        raise HTTPException(status_code=400, detail='Table not found.')
