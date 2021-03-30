from fastapi import FastAPI

from ops import ClientFactory, TableManager, EntityManger
from utils import Response
from resources import BaseError, QueryEntitiesError

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tables")
def create_table(table_name: str):
    client = ClientFactory.getTableServiceClient()
    result = TableManager.create_table(client, table_name)
    if not result:
        return Response.error(400, 'Table already exists.')
    return Response.ok()


@app.delete("/tables")
def delete_table(table_name: str):
    client = ClientFactory.getTableServiceClient()
    result = TableManager.delete_table(client, table_name)
    if not result:
        return Response.error(400, 'Table does not exist.')
    return Response.ok()


@app.get("/entities")
def query_entities(table_name: str):
    def _query_entities():
        client = ClientFactory.getTableClient(table_name)

        result = EntityManger.query_entities(client)
        if not result:
            return QueryEntitiesError
        data = [item for item in result]
        return data

    return runWithErrorHandling(_query_entities)


@app.post("/entities")
def create_entity(table_name: str, row_key: str):
    client = ClientFactory.getTableClient(table_name)
    result = EntityManger.create_entity(client, row_key)
    if not result:
        return Response.error(400, 'Entity already exists.')
    return Response.ok()


@app.delete("/entities")
def delete_entity(table_name: str, row_key: str, partition_key: str):
    client = ClientFactory.getTableClient(table_name)
    result = EntityManger.delete_entity(client, row_key, partition_key)
    if not result:
        return Response.error(400, 'Entity does not exist.')
    return Response.ok()

def runWithErrorHandling(fn):
    try:
        return Response.ok(fn())
    except BaseError as error:
        raise Response.error(error.code, error.message)