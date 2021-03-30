from src.ops import ClientFactory, TableManager
from src.resources import Config


class MockTable:
    @staticmethod
    @property
    def table_name():
        return 'name'


class TestTableManager:
    def create_table(*args, **kwargs):
        return MockTable

    def get_connection_string(*args, **kwargs):
        return ''

    def test_create_table(self, monkeypatch):
        client = ClientFactory.getTableServiceClient()
        monkeypatch.setattr(client, 'create_table', self.create_table)
        monkeypatch.setattr(Config, 'get_connection_string', self.get_connection_string)

        assert TableManager.create_table(client, 'name')

    def test_delete_table(self, monkeypatch):
        client = ClientFactory.getTableServiceClient()
        monkeypatch.setattr(client, 'delete_table', self.create_table)
        monkeypatch.setattr(Config, 'get_connection_string', self.get_connection_string)
        
        assert TableManager.delete_table(client, 'name')
