import uuid
from module.ingestion import Ingestion


ingestion = Ingestion()
ingestion.process(
    payload={
        "cdTipoIngestao": "Avro",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "avro_db",
        "nmTabela": "tbl_avro",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Bin",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "bin_db",
        "nmTabela": "tbl_bin",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Csv",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "csv_db",
        "nmTabela": "tbl_csv",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Json",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "json_db",
        "nmTabela": "tbl_json",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Orc",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "orc_db",
        "nmTabela": "tbl_orc",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Parquet",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "parquet_db",
        "nmTabela": "tbl_parquet",
    }
)
ingestion.process(
    payload={
        "cdTipoIngestao": "Xlsx",
        "cdIngestao": int(uuid.uuid4()),
        "nmDatabase": "xlsx_db",
        "nmTabela": "tbl_xlsx",
    }
)
