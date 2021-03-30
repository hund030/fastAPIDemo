from typing import Optional

from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceExistsError

from utils import Validation


class TableManager(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_table(client: TableServiceClient, name: str) -> bool:
        if not Validation.validateTableName(name):
            print("Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long.")
            return False

        try:
            table_item = client.create_table(
                table_name=name)
            print("Created table {}!".format(table_item.table_name))
            return True
        except ResourceExistsError:
            print("Table already exists.")
            return False

    @staticmethod
    def delete_table(client: TableServiceClient, name: str) -> bool:
        try:
            client.delete_table(table_name=name)
            print("Deleted table {}!".format(name))
            return True
        except ResourceNotFoundError:
            print("Table does not exist.")
            return False
