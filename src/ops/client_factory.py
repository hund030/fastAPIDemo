from resources import Config


class ClientFactory(object):

    @staticmethod
    def getTableServiceClient():
        from azure.data.tables import TableServiceClient
        return TableServiceClient.from_connection_string(
            Config.get_connection_string())

    @staticmethod
    def getTableClient(table_name):
        from azure.data.tables import TableClient
        return TableClient.from_connection_string(
            Config.get_connection_string(), table_name)
