class BaseError(Exception):
    pass

class TableNameValidationError(BaseError):
    def __init__(self):
        self.code = 400
        self.message = "Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long."

class TableAlreadyExistsError(BaseError):
    def __init__(self):
        self.code = 400
        self.message = "Table already exists."

class TableNotFoundError(BaseError):
    def __init__(self):
        self.code = 400
        self.message = "Table does not exist."

class EntityAlreadyExistsError(BaseError):
    def __init__(self):
        self.code = 400
        self.message = "Entity already exists."

class EntityNotFoundError(BaseError):
    def __init__(self):
        self.code = 400
        self.message = "Entity does not exist."

class QueryEntitiesError(BaseError):
    def __init__(self):
        self.code = 500
        self.message = "Cannot query entities."