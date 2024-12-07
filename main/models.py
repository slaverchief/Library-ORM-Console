from abc import abstractmethod, ABC
from .exceptions import InvalidInput


class BaseModel(ABC):

    @abstractmethod
    def __init__(self, deserializing: bool = False, id: str = None):
        if deserializing:
            self.id = int(id)




