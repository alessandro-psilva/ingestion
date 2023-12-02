from model.imports import *


class Parquet(Factory):
    def process_data(self) -> Data:
        print(f"ProcessandoParquet: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
