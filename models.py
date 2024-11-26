import json

from exceptions import ObjectsDontExist, InvalidInput


class Book:
    __pk = 0
    __file_name = 'models_data.json'

    def __str__(self):
        return f"Книга: " \
                f"id: {self.id} |" \
                f" название: {self.title} |" \
                f" автор: {self.author} |" \
                f" год: {self.year} |" \
                f" статус: {"В наличии" if self.status else "Выдана"}"

    def __init__(self, title: str, author: str, year: int, deserializing: bool = False, id: str = None, status: bool = None):
        if deserializing:
            year = int(year)
            self.status = status
            self._id = int(id)
        else:
            self._id = Book.__pk
            Book.__pk += 1
            self.status = True
        self.title = title
        self.author = author
        if not isinstance(year, int):
            raise InvalidInput("невалидное значение year")
        self.year = year

    @staticmethod
    def get_by_id(id: int):
        if not isinstance(id, int) or id < 0:
            raise InvalidInput('невалидный ID')
        id = str(id)
        with open(Book.get_file_name(), 'r') as f:
            data = json.load(f)
            try:
                return Book.deserialize_object(data[id])
            except KeyError:
                raise ObjectsDontExist("несуществующий ID")

    @staticmethod
    def deserialize_object(data: dict, filter_data: dict = None):
        if filter_data:
            for key in filter_data.keys():
                try:
                    if data[key] != filter_data[key]:
                        return
                except KeyError:
                    raise InvalidInput("введен невалидный фильтр")
        b = Book(**data, deserializing=True)
        return b

    @staticmethod
    def deserialize(json: dict, filter_data: dict = None) -> list:
        ret_list = []
        for id in json.keys():
            data = json.get(id)
            b = Book.deserialize_object(data, filter_data)
            if b:
                ret_list.append(b)
        return ret_list

    @staticmethod
    def initialize():
        try:
            with open(Book.get_file_name(), 'r') as f:
                data = json.load(f)
                if data.keys():
                    Book.__pk = max(map(int,data.keys()))+1
        except FileNotFoundError:
            with open(Book.get_file_name(), 'w') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

    @staticmethod
    def get_file_name() -> str:
        return Book.__file_name

    @staticmethod
    def list_objects(**kwargs) -> list:
        with open(Book.get_file_name(), 'r') as f:
            data = json.load(f)
            books = Book.deserialize(data, filter_data=kwargs)
            if not books:
                raise ObjectsDontExist("нет объектов с указанными параметрами")
            return books

    def get_serialized(self) -> dict:
        return {"id": self.id,
                "title": self.title,
                "author": self.author,
                "year": self.year,
                "status": self.status
                }

    def delete(self):
        data = {}
        with open(Book.get_file_name(), 'r') as f:
            data = json.load(f)
            del data[str(self.id)]
        with open(Book.get_file_name(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def save(self):
        data = {}
        with open(Book.get_file_name(), 'r') as f:
            data = json.load(f)
            data[str(self.id)] = self.get_serialized()
        with open(Book.get_file_name(), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @property
    def id(self):
        return self._id

