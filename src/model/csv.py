from module.factory import Factory
from module.schema import Schema
from module.data import Data
from typing import Dict


class Csv(Factory):
    def __init__(self, payload: Dict) -> None:
        self._payload = payload
        super().__init__(payload)

    def process_data(self) -> Data:
        print(f"Processando {self._payload}")

    def generate_schema(self) -> Schema:
        pass
