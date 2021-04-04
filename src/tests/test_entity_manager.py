from ops import ClientFactory, EntityManger
from resources import Config
from tests.helper import TestHelper


class MockEntity:
    pass


class TestEntityManager:
    def create_entity(*args, **kwargs):
        return MockEntity

    def query_entities(*args, **kwargs):
        return []

    def delete_entity(*args, **kwargs):
        return

    def test_create_entity(self, monkeypatch):
        monkeypatch.setattr(Config, 'get_connection_string',
                            TestHelper.get_connection_string)
        client = ClientFactory.getTableClient('name')
        monkeypatch.setattr(client, 'create_entity', self.create_entity)

        assert EntityManger.create_entity(client, 'row_key', 'name')

    def test_query_entities(self, monkeypatch):
        monkeypatch.setattr(Config, 'get_connection_string',
                            TestHelper.get_connection_string)
        client = ClientFactory.getTableClient('name')
        monkeypatch.setattr(client, 'query_entities', self.query_entities)

        assert EntityManger.query_entities(client) == []

    def test_delete_entity(self, monkeypatch):
        monkeypatch.setattr(Config, 'get_connection_string',
                            TestHelper.get_connection_string)
        client = ClientFactory.getTableClient('name')
        monkeypatch.setattr(client, 'delete_entity', self.delete_entity)

        assert EntityManger.delete_entity(client, 'row_key', 'partition_key')
