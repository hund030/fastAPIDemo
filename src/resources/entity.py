from datetime import date
import copy
from resources import Constants


class Entity(object):

    entity_template = {
        u"PartitionKey": u"pk",
        u"RowKey": u"row",
        u"No.": u"No.",
        u"Name": u"Name",
        u"Authors": [u"Authors"],
        u"Main Actors": [u"Main Actors"],
        u"Directors": [u"Directors"],
        u"Publication Date": date.fromisoformat(Constants.Default_Date),
        u"Tags": [u"Tags"],
    }

    @staticmethod
    def newEntity():
        return copy.deepcopy(Entity.entity_template)
