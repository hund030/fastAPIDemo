from azure.core.exceptions import ResourceNotFoundError
from azure.core.paging import ItemPaged
from azure.data.tables import TableClient
from datetime import date
from resources import Constants, Entity, EntityAlreadyExistsError, EntityNotFoundError


class EntityManger(object):
    @staticmethod
    def create_entity(client: TableClient, row_key: str,  parameters=''):
        e = Entity.newEntity(parameters)
        e[u"RowKey"] = row_key

        try:
            client.create_entity(entity=e)
        except ResourceExistsError:
            raise EntityAlreadyExistsError()

    @staticmethod
    def query_entities(client: TableClient) -> ItemPaged:
        queried_entities = client.query_entities(filter="")
        return queried_entities

    @staticmethod
    def delete_entity(client: TableClient, row_key: str, partition_key: str):
        try:
            client.delete_entity(row_key=row_key, partition_key=partition_key)
        except ResourceNotFoundError:
            raise EntityNotFoundError()
