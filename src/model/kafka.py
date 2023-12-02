from model.imports import *


class Kafka(Factory):
    def process_data(self) -> Data:
        print(f"ProcessandoKafka: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass
