class BaseError(Exception):
    pass


class UserError(BaseError):
    def __init__(self):
        self.code = 400


class SystemError(BaseError):
    def __init__(self):
        self.code = 500


class TableNameValidationError(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Table names must be alphanumeric, cannot begin with a number, and must be between 3-63 characters long.'


class TableAlreadyExistsError(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Table already exists.'


class TableNotFoundError(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Table does not exist.'


class EntityAlreadyExistsError(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Entity already exists.'


class EntityNotFoundError(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Entity does not exist.'


class QueryEntitiesError(SystemError):
    def __init__(self):
        super().__init__()
        self.message = 'Cannot query entities.'


class InvalidParameterFormat(UserError):
    def __init__(self):
        super().__init__()
        self.message = 'Invalid parameters format, please pass a JSON format string.'
