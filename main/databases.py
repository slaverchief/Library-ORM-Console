import json
from abc import ABC
from main.exceptions import ObjectsDontExist, InvalidInput
from main.serializers import ModelSerializer
import pathlib
import os

class JSONDB():
    __pk = 0

    def __init__(self, model):
        self.__model = model
        curdir = pathlib.Path().resolve()
        save_dir = os.path.join(curdir, 'databases_data')
        self.__file_name = f"{save_dir}/{self.__model.__name__}_model_data.json"
        if not self.__file_name:
            raise SystemError("Не прописано название файла базы данных.")
        try:
            with open(self.__file_name, 'r') as f:
                data = json.load(f)
                if data.keys():
                    JSONDB.__pk = max(map(int,data.keys()))+1
        except FileNotFoundError:
            with open(self.__file_name, 'w') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

    def read(self):
        with open(self.__file_name, 'r') as f:
            data = json.load(f)
            return data

    def get_object(self, id: int):
        if id < 0:
            raise InvalidInput("невалидное значение идентификатора")
        return self.list_objects(id=id)[0]

    def list_objects(self, **kwargs) -> list:
        data = self.read()
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
        with open(self.__file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_object(self, obj):
        data = self.read()
        data.pop(str(obj.id))
        with open(self.__file_name, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)