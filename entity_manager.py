from azure.data.tables import TableClient

entity = {
    u'PartitionKey': u'color',
    u'RowKey': u'brand',
    u'text': u'Marker',
    u'color': u'Purple',
    u'price': u'5'
}


class EntityManger(object):
    @staticmethod
    def create_entity(client: TableClient) -> bool:
        from azure.core.exceptions import ResourceExistsError
        try:
            client.create_entity(entity=entity)
            return True
        except ResourceExistsError:
            print("Entity already exists.")
            return False

    @staticmethod
    def delete_entity(client: TableClient) -> bool:
        from azure.core.exceptions import ResourceNotFoundError
        try:
            client.delete_entity(row_key=entity["RowKey"],
                                 partition_key=entity["PartitionKey"])
            return True
        except ResourceNotFoundError:
            print("Entity does not exists.")
            return False
