from model.imports import *


class Csv(Factory):
    def process_data(self) -> Data:
        print(f"ProcessandoCsv: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
