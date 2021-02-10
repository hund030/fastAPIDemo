from typing import Optional

from azure.data.tables import TableServiceClient

from utils import Utils


class TableManager(object):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_table(client: TableServiceClient, name: str) -> bool:
        if not Utils.validateTableName(name):
            print("Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long.")
            return False

        from azure.core.exceptions import ResourceExistsError
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
        from azure.core.exceptions import ResourceNotFoundError
        try:
            client.delete_table(table_name=name)
            print("Deleted table {}!".format(name))
            return True
        except ResourceNotFoundError:
            print("Table not found.")
            return False
