from model.imports import *


class Orc(Factory):
    def __init__(self, payload: Dict) -> None:
        super().__init__(payload)

    def process_data(self) -> Data:
        print(f"ProcessandoOrc: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
