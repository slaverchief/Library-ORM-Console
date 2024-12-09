from abc import ABC, abstractmethod

class DatabaseUnit(ABC):
    __pk = 0

    @abstractmethod
    def get_object(self, id):
        pass

    @abstractmethod
    def list_objects(self, **kwargs):
        pass

    @abstractmethod
    def add_or_update_object(self, obj):
        pass

    @abstractmethod
    def delete_object(self, obj):
        pass
