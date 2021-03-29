import re


class Validation(object):
    @staticmethod
    def validateTableName(name: str) -> bool:
        result = re.match(r'^[a-zA-Z][a-zA-Z0-9]{2,62}$', name)
        br = bool(result)
        return br
