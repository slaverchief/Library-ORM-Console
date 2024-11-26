import json

from exceptions import ObjectsDontExist, InvalidInput


class BaseModel:
    __pk = 0
    _file_name = None



    def __init__(self, deserializing: bool = False, id: str = None):
        if deserializing:
            self._id = int(id)
        else:
            self._id = type(self).__pk
            type(self).__pk += 1



    @classmethod
    def get_by_id(cls, id: int):
        if not isinstance(id, int) or id < 0:
            raise InvalidInput('невалидный ID')
        id = str(id)
        with open(cls.get_file_name(), 'r') as f:
            data = json.load(f)
            try:
                return cls.deserialize_object(data[id])
            except KeyError:
                raise ObjectsDontExist("несуществующий ID")

    @classmethod
    def deserialize_object(cls, data: dict, filter_data: dict = None):
        if filter_data:
            for key in filter_data.keys():
                try:
                    if data[key] != filter_data[key]:
                        return
                except KeyError:
                    raise InvalidInput("введен невалидный фильтр")
        b = cls(**data, deserializing=True)
        return b

    @classmethod
    def deserialize(cls, json: dict, filter_data: dict = None) -> list:
        ret_list = []
        for id in json.keys():
            data = json.get(id)
            b = cls.deserialize_object(data, filter_data)
            if b:
                ret_list.append(b)
        return ret_list

    @classmethod
    def initialize(cls):
        if not cls._file_name:
            raise SystemError("Была инициализирована невалидная модель")
        try:
            with open(cls.get_file_name(), 'r') as f:
                data = json.load(f)
                if data.keys():
                    cls.__pk = max(map(int,data.keys()))+1
        except FileNotFoundError:
            with open(cls.get_file_name(), 'w') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

    @classmethod
    def get_file_name(cls) -> str:
        return cls._file_name

    @classmethod
    def list_objects(cls, **kwargs) -> list:
        with open(cls.get_file_name(), 'r') as f:
            data = json.load(f)
            books = cls.deserialize(data, filter_data=kwargs)
            if not books:
                raise ObjectsDontExist("нет объектов с указанными параметрами")
            return books

    def get_serialized(self) -> dict:
        serialized_dict = {"id": self.id}
        return serialized_dict

    def delete(self):
        data = {}
        with open(type(self).get_file_name(), 'r') as f:
            data = json.load(f)
            del data[str(self.id)]
        with open(type(self).get_file_name(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save(self):
        data = {}
        with open(type(self).get_file_name(), 'r') as f:
            data = json.load(f)
            data[str(self.id)] = self.get_serialized()
        with open(type(self).get_file_name(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @property
    def id(self):
        return self._id


class Book(BaseModel):
    _file_name = "book_models_data.json"

    def __init__(self, title: str, author: str, year: int, status: bool = None, deserializing: bool = False, id: str = None):
        super().__init__(deserializing, id)
        if deserializing:
            year = int(year)
            self.status = status
        else:
            self.status = True
        self.title = title
        self.author = author
        if not isinstance(year, int):
            raise InvalidInput("невалидное значение year")
        self.year = year

    def __str__(self):
        return f"Книга: " \
                f"id: {self.id} |" \
                f" название: {self.title} |" \
                f" автор: {self.author} |" \
                f" год: {self.year} |" \
                f" статус: {"В наличии" if self.status else "Выдана"}"

    def get_serialized(self) -> dict:
        serialized_dict = super().get_serialized()
        concat_dict = {
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "status": self.status
                }
        return serialized_dict | concat_dict


