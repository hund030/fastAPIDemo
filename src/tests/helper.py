class TestHelper:
    @staticmethod
    def get_connection_string():
        return 'DefaultEndpointsProtocol=https;AccountName={};AccountKey={}'.format('accountName', 'accountKey')