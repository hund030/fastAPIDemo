from config import Config


class ClientFactory(object):

    @staticmethod
    def getTableServiceClient():
        from azure.data.tables import TableServiceClient
        return TableServiceClient.from_connection_string(
            Config.get_connection_string())
