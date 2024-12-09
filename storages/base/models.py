from abc import abstractmethod, ABC
from core.exceptions import InvalidInput


class Model(ABC):

    @abstractmethod
    def __init__(self, deserializing: bool = False, id: str = None):
        if deserializing:
            self.id = int(id)




