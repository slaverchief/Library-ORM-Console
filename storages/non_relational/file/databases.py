from storages.base.models import Model
from .units import JSONUnit
from typing import Type

class JSONDB:

    @staticmethod
    def get_unit(model: Type[Model]) -> JSONUnit:
        return JSONUnit(model)


