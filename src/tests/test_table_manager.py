from src.ops import ClientFactory, TableManager
from src.resources import Config
from src.tests.helper import TestHelper

class MockTable:
    @staticmethod
    @property
    def table_name():
        return 'name'


class TestTableManager:
    def create_table(*args, **kwargs):
        return MockTable

    def test_create_table(self, monkeypatch):
        monkeypatch.setattr(Config, 'get_connection_string', TestHelper.get_connection_string)
        client = ClientFactory.getTableServiceClient()
        monkeypatch.setattr(client, 'create_table', self.create_table)

        assert TableManager.create_table(client, 'name')

    def test_delete_table(self, monkeypatch):
        monkeypatch.setattr(Config, 'get_connection_string', TestHelper.get_connection_string)
        client = ClientFactory.getTableServiceClient()
        monkeypatch.setattr(client, 'delete_table', self.create_table)
        
        assert TableManager.delete_table(client, 'name')
