from model.imports import *


class Parquet(Factory):
    def __init__(self, payload: Dict) -> None:
        self._payload = payload
        super().__init__(payload)

    def process_data(self) -> Data:
        print(f"ProcessandoParquet: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
