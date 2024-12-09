from storages.base.models import Model
from core.exceptions import InvalidInput

class Book(Model):

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