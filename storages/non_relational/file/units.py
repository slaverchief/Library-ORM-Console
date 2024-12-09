import json
from storages.base.units import DatabaseUnit
from core.exceptions import ObjectsDontExist, InvalidInput
from .serializers import ModelSerializer
from abc import abstractmethod
from .constants import FILES_DIRECTORY

class FileUnit(DatabaseUnit):

    def __init__(self, model):
        self.__model = model
        self._file_name = f"{FILES_DIRECTORY}/{self.__model.__name__}_model_data.json"
        if not self._file_name:
            raise SystemError("Не прописано название файла базы данных.")
        try:
            with open(self._file_name, 'r') as f:
                data = json.load(f)
                if data.keys():
                    type(self).__pk = max(map(int,data.keys()))+1
        except FileNotFoundError:
            with open(self._file_name, 'w') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

    @abstractmethod
    def read_into_dict(self):
        pass

    def list_objects(self, **kwargs) -> list:
        data = self.read_into_dict()
        objects = ModelSerializer.deserialize(data, self.__model)
        result = []
        for obj in objects:
            to_add = True
            for key in kwargs.keys():
                if obj.__dict__[key] != kwargs[key]:
                    to_add = False
                    break
            if to_add:
                result.append(obj)
        if not result:
            raise ObjectsDontExist("нет объектов с указанными параметрами")
        return result

    def get_object(self, id: int):
        if id < 0:
            raise InvalidInput("невалидное значение идентификатора")
        return self.list_objects(id=id)[0]



class JSONUnit(FileUnit):

    def read_into_dict(self):
        with open(self._file_name, 'r') as f:
            data = json.load(f)
            return data

    def add_or_update_object(self, obj):
        data = self.read()
        object_id = 0
        if data:
            if str(obj.id) in data.keys():
                object_id = obj.id
            else:
                object_id = max(map(int, data))+1
        obj.id = object_id
        data[str(obj.id)] = ModelSerializer.serialize(obj)
        with open(self._file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_object(self, obj):
        data = self.read()
        data.pop(str(obj.id))
        with open(self._file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)