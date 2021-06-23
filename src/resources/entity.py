from datetime import date
import copy
from resources import DefaultValues, InvalidParameterFormat
import json
import uuid


class Entity(object):

    entity_template = {
        u'PartitionKey': u'pk',
        u'RowKey': u'row',
        u'No.': u'No.',
        u'Name': u'Name',
        u'Authors': '["Authors"]',
        u'MainActors': '["Main Actors"]',
        u'Directors': '["Directors"]',
        u'PublicationDate': date.fromisoformat(DefaultValues.Default_Date).strftime(DefaultValues.Date_Format),
        u'Tags': '["Tags"]'
    }

    @staticmethod
    def newEntity(parameters_string):
        try:
            parameters = json.loads(parameters_string)
        except BaseException as error:
            raise InvalidParameterFormat()

        entity = copy.deepcopy(Entity.entity_template)
        entity[u'RowKey'] = str(uuid.uuid4())
        for attr, value in parameters.items():
            entity[attr] = value
        return entity
