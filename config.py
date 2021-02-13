account_name = 'mylibrary030'
account_key = '5A+DFIq31sIXE0CU9rZwT04p/xn9OXb7Cw36IKfI77o7YkX33SWGnFQHf3DUXcWeV0RbcDH3NiqdXhv4urDTBg=='
connection_string = 'DefaultEndpointsProtocol=[http|https];AccountName=%s;AccountKey=%s' % (account_name, account_key)
class Config:
    @staticmethod
    def get_connection_string():
        return connection_string
