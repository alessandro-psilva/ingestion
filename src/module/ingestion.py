from module.imports import *


class Ingestion:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def process(self, payload: Dict) -> Dict:
        self._payload: Dict = payload
        self._payload["cdIngestao"] = int(uuid.uuid4())
        self._model: Union[Avro, Bin, Csv, Json, Orc, Parquet, Xlsx, Kafka] = eval(
            payload["cdTipoIngestao"]
        )
        self._model(payload=self._payload).process_data()
        del self._model
