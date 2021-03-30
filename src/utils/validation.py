import re
from resources import TableNameValidationError


class Validation(object):
    @staticmethod
    def validateTableName(name: str) -> bool:
        result = re.match(r'^[a-zA-Z][a-zA-Z0-9]{2,62}$', name)
        if not result:
            raise TableNameValidationError()
