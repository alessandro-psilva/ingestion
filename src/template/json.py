from template.imports import *


class Json(Factory):
    def process_data(self) -> Data:
        print(f"ProcessandoJson: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass