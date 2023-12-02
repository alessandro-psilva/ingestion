from model.imports import *


class Avro(Factory):
    def __init__(self, payload: Dict) -> None:
        super().__init__(payload)

    def process_data(self) -> Data:
        print(f"ProcessandoAvro: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
