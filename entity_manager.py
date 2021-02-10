from azure.data.tables import TableClient
import random
import copy

brands = [u"Crayola", u"Sharpie", u"Chameleon"]
colors = [u"red", u"blue", u"orange", u"yellow"]
names = [u"marker", u"pencil", u"pen"]
entity_template = {
    u"PartitionKey": u"pk",
    u"RowKey": u"row",
}


class EntityManger(object):
    @staticmethod
    def create_entity(client: TableClient, row_key: str) -> bool:
        e = copy.deepcopy(entity_template)
        e[u"RowKey"] = row_key
        e[u"Name"] = random.choice(names)
        e[u"Brand"] = random.choice(brands)
        e[u"Color"] = random.choice(colors)
        e[u"Value"] = random.randint(0, 100)

        from azure.core.exceptions import ResourceExistsError
        try:
            client.create_entity(entity=e)
            return True
        except ResourceExistsError:
            print("Entity already exists.")
            return False

    @staticmethod
    def query_entities(client: TableClient) -> list:
        queried_entities = client.query_entities(filter="")
        for entity_chosen in queried_entities:
            print(entity_chosen)
        return queried_entities

    @staticmethod
    def delete_entity(client: TableClient, row_key: str, partition_key: str) -> bool:
        from azure.core.exceptions import ResourceNotFoundError
        try:
            client.delete_entity(row_key=row_key, partition_key=partition_key)
            return True
        except ResourceNotFoundError:
            print("Entity does not exist.")
            return False
