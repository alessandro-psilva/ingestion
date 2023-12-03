from template.imports import *


class Parquet(Factory):
    def process_data(self) -> Data:
        self._get_bastao
        print(f"Processando: {self._payload.cdTipoIngestao}")

    def generate_schema(self) -> Schema:
        pass

    @property
    def _get_bastao(self) -> None:
        self._payload.set_attr("nmArquivoBastao", "ArquivoBastao.bin")
