import os
from resources import EnvKey

STORAGE_ACCOUNT_NAME = os.getenv(EnvKey.Storage_Account_Name)
STORAGE_ACCOUNT_KEY = os.getenv(EnvKey.Storage_Account_Key)

class Config(object):
    @staticmethod
    def get_connection_string():
        return 'DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix=core.windows.net'.format(
            STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY
        )
