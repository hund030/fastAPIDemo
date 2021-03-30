from resources import Config
from utils import Validation

class ClientFactory(object):

    @staticmethod
    def getTableServiceClient():
        from azure.data.tables import TableServiceClient
        return TableServiceClient.from_connection_string(
            Config.get_connection_string())

    @staticmethod
    def getTableClient(table_name):
        from azure.data.tables import TableClient

        if not Validation.validateTableName(table_name):
            print("Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long.")
            return False
        
        return TableClient.from_connection_string(
            Config.get_connection_string(), table_name)
