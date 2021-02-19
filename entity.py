from datetime import date
import copy


class Entity(object):

    entity_template = {
        u"PartitionKey": u"pk",
        u"RowKey": u"row",
        u"No.": u"No.",
        u"Name": u"Name",
        u"Authors": [u"Authors"],
        u"Main Actors": [u"Main Actors"],
        u"Directors": [u"Directors"],
        u"Publication Date": date.fromisoformat('2012-2-29'),
        u"Tags": [u"Tags"],
    }

    @staticmethod
    def newEntity():
        return copy.deepcopy(entity_template)
