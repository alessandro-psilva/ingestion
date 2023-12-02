from module.ingestion import Ingestion


ingestion = Ingestion()
ingestion.process(payload={'cdTipoIngestao': 'Avro'})
ingestion.process(payload={'cdTipoIngestao': 'Bin'})
ingestion.process(payload={'cdTipoIngestao': 'Csv'})
ingestion.process(payload={'cdTipoIngestao': 'Json'})
ingestion.process(payload={'cdTipoIngestao': 'Orc'})
ingestion.process(payload={'cdTipoIngestao': 'Parquet'})
ingestion.process(payload={'cdTipoIngestao': 'Xlsx'})
