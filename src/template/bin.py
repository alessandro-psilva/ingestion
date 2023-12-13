from template.imports import *


class Bin(Factory):
    def process_data(self) -> Data:
        self._get_control
        print(f"Processando: {self._payload.cdTipoIngestao}")

    def generate_schema(self) -> Schema:
        pass

    @property
    def _get_control(self) -> None:
        self._payload.set_attr("nmArquivoControle", "ArquivoControle.bin")
