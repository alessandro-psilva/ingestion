from model.imports import *


class Xlsx(Factory):
    def process_data(self) -> Data:
        print(f"ProcessandoXlsx: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
