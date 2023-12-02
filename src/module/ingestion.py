import uuid
from model.avro import Avro
from model.bin import Bin
from model.csv import Csv
from model.json import Json
from model.orc import Orc
from model.parquet import Parquet
from model.xlsx import Xlsx
from typing import Dict, Union


class Ingestion:
    def process(self, payload: Dict) -> Dict:
        self._payload: Dict = payload
        self._payload["cdIngestao"] = int(uuid.uuid4())
        self._factory: Union[Avro, Bin, Csv, Json, Orc, Parquet, Xlsx] = eval(
            payload["cdTipoIngestao"]
        )
        self._factory(payload=self._payload).process_data()
