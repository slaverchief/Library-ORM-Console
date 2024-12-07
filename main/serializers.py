
class ModelSerializer:

    @staticmethod
    def deserialize(json: dict, model) -> list:
        objects = []
        for id in json.keys():
            data = json.get(id)
            objects.append(model(**data, deserializing=True))
        return objects

    @staticmethod
    def serialize(obj) -> dict:
        serialized_dict = {}
        object_dict = obj.__dict__
        for key in object_dict:
            serialized_dict[key] = object_dict[key]
        return serialized_dict


