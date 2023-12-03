from module.imports import *


class Ingestion:
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def process(self, payload: Dict) -> Dict:
        payload["cdIngestao"] = int(uuid.uuid4())
        self._payload: Payload = Payload(**payload)
        self._template: Union[Avro, Bin, Csv, Json, Orc, Parquet, Xlsx, Kafka] = eval(
            self._payload.cdTipoIngestao
        )
        self._template(payload=self._payload).process_data()
        del self._template
