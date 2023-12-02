from abc import ABC, abstractmethod
from typing import Dict
from module.schema import Schema
from module.data import Data


class Factory(ABC):
    def __init__(self, payload: Dict) -> None:
        super().__init__()

    @abstractmethod
    def process_data(self) -> Data:
        pass

    @abstractmethod
    def generate_schema(self) -> Schema:
        pass

    def __del__(self) -> None:
        print(f"Delete: {self.__str__}")
