from template.imports import *


class Parquet(Factory):
    def process_data(self) -> Data:
        self._get_bastao
        print(f"ProcessandoParquet: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass

    @property
    def _get_bastao(self) -> None:
        self._payload["nmArquivoBastao"] = "ArquivoBastao.bin"
