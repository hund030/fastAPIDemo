class BaseError(Exception):
    pass

class TableNameValidationError(BaseError):
    def __init__(self):
        self.message = "Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long."
        self.code = 400

class QueryEntitiesError(BaseError):
    def __init__(self):
        self.code = 500
        self.message = "Cannot query entities."