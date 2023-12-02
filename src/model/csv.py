import json
from model.factory import Factory
from module.schema import Schema
from module.data import Data
from typing import Dict


class Csv(Factory):
    def __init__(self, payload: Dict) -> None:
        self._payload = payload
        super().__init__(payload)

    def process_data(self) -> Data:
        print(f"ProcessandoCsv: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
