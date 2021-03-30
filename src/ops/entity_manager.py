from azure.core.exceptions import ResourceNotFoundError
from azure.core.paging import ItemPaged
from azure.data.tables import TableClient
from datetime import date
from src.resources import Constants, Entity


class EntityManger(object):
    @staticmethod
    def create_entity(client: TableClient, row_key: str,  name: str,
                      id: str = '', author=[''], actors=[''], directors=[''], tags=[''],
                      publication_date=date.fromisoformat(Constants.Default_Date)) -> bool:
        e = Entity.newEntity()
        e[u"RowKey"] = row_key
        e[u"Name"] = name

        try:
            client.create_entity(entity=e)
            return True
        except ResourceExistsError:
            print("Entity already exists.")
            return False

    @staticmethod
    def query_entities(client: TableClient) -> ItemPaged:
        queried_entities = client.query_entities(filter="")
        return queried_entities

    @staticmethod
    def delete_entity(client: TableClient, row_key: str, partition_key: str) -> bool:
        try:
            client.delete_entity(row_key=row_key, partition_key=partition_key)
            return True
        except ResourceNotFoundError:
            print("Entity does not exist.")
            return False
