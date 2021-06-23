from resources import BaseError
from utils import Response
from ops import ClientFactory, TableManager, EntityManger
from azure.core.exceptions import AzureError
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.post('/tables')
def create_table(table_name: str):
    def _create_table():
        client = ClientFactory.getTableServiceClient()
        TableManager.create_table(client, table_name)
    return runWithErrorHandling(_create_table)


@app.delete('/tables')
def delete_table(table_name: str):
    def _delete_table():
        client = ClientFactory.getTableServiceClient()
        TableManager.delete_table(client, table_name)
    return runWithErrorHandling(_delete_table)


@app.get('/entities')
def query_entities(table_name: str, parameters=''):
    def _query_entities():
        client = ClientFactory.getTableClient(table_name)
        result = EntityManger.query_entities(client)
        data = [item for item in result]
        return data

    return runWithErrorHandling(_query_entities)


@app.post('/entities')
def create_entity(table_name: str, row_key: str, parameters=''):
    def _create_entity():
        client = ClientFactory.getTableClient(table_name)
        EntityManger.create_entity(client, row_key)
    return runWithErrorHandling(_create_entity)


@app.delete('/entities')
def delete_entity(table_name: str, row_key: str, partition_key: str):
    def _delete_entity():
        client = ClientFactory.getTableClient(table_name)
        EntityManger.delete_entity(client, row_key, partition_key)
    return runWithErrorHandling(_delete_entity)


def runWithErrorHandling(fn):
    try:
        return Response.ok(fn())
    except BaseError as error:
        raise Response.error(error.code, error.message)
    except AzureError as error:
        raise Response.error(400, 'Get Azure error: {}'.format(error))
    except BaseException as error:
        raise Response.error(500, 'Unhandled exception: {}.'.format(error))
