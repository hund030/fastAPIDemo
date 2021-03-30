from typing import Optional

from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceExistsError

from resources import TableAlreadyExistsError, TableNotFoundError
from utils import Validation


class TableManager(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_table(client: TableServiceClient, name: str):
        Validation.validateTableName(name)

        try:
            table_item = client.create_table(
                table_name=name)
            print("Created table {}!".format(table_item.table_name))
        except ResourceExistsError:
            raise TableAlreadyExistsError()

    @staticmethod
    def delete_table(client: TableServiceClient, name: str):
        try:
            client.delete_table(table_name=name)
            print("Deleted table {}!".format(name))
        except ResourceNotFoundError:
            raise TableNotFoundError()
