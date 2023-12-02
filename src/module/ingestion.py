from module.imports import *


class Ingestion:
    def process(self, payload: Dict) -> Dict:
        self._payload: Dict = payload
        self._payload["cdIngestao"] = int(uuid.uuid4())
        self._model: Union[Avro, Bin, Csv, Json, Orc, Parquet, Xlsx, Kafka] = eval(
            payload["cdTipoIngestao"]
        )
        self._model(payload=self._payload).process_data()
