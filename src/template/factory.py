from abc import ABC, abstractmethod
from module.schema import Schema
from module.data import Data
from module.payload import Payload


class Factory(ABC):
    def __init__(self, payload: Payload) -> None:
        super().__init__()
        try:
            if not isinstance(payload, Payload):
                raise TypeError("Payload must be a Payload.")
            self._payload = payload
        except Exception as e:
            print(f"Error: {e}")

    @abstractmethod
    def process_data(self) -> Data:
        pass

    @abstractmethod
    def generate_schema(self) -> Schema:
        pass

    def __del__(self) -> None:
        print(f"Delete: {self.__class__.__name__}")
