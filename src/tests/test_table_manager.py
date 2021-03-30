from src.ops import ClientFactory

class TestTableManager:
    def test_create_table(self):
        client = ClientFactory.getTableServiceClient()
        assert True

    def test_delete_table(self):
        assert True 