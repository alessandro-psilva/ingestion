from template.imports import *


class Kafka(Factory):
    def process_data(self) -> Data:
        print(f"Processando: {self._payload.cdTipoIngestao}")

    def generate_schema(self) -> Schema:
        pass
