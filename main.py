from response import Response

from fastapi import FastAPI

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
    client = ClientFactory.getTableClient(table_name)
    result = EntityManger.query_entities(client)
    if not result:
        return Response.error(500, 'Cannot query entities.')
    data = [item for item in result]
    return Response.ok(data)


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
