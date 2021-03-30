from resources import Config, TableNameValidationError
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

        Validation.validateTableName(table_name)
        
        return TableClient.from_connection_string(
            Config.get_connection_string(), table_name)
