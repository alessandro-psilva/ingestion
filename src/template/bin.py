from template.imports import *


class Bin(Factory):
    def process_data(self) -> Data:
        self._get_control
        print(f"ProcessandoBin: {json.dumps(self._payload, indent=2)}")

    def generate_schema(self) -> Schema:
        pass

    @property
    def _get_control(self) -> None:
        self._payload["nmArquivoControle"] = "ArquivoControle.bin"