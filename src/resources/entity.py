from datetime import date
import copy
from resources import Constants, InvalidParameterFormat
import json
import uuid


class Entity(object):

    entity_template = {
        u 'PartitionKey ': u 'pk ',
        u 'RowKey ': u 'row ',
        u 'No. ': u 'No. ',
        u 'Name ': u 'Name ',
        u 'Authors ': [u 'Authors '],
        u 'Main Actors ': [u 'Main Actors '],
        u 'Directors ': [u 'Directors '],
        u 'Publication Date ': date.fromisoformat(Constants.Default_Date),
        u 'Tags ': [u 'Tags '],
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
