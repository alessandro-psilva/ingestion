import json
from module.ingestion import Ingestion


with open("src/data/payloads.json", "r") as arq:
    payloads = json.load(arq)

ingestion = Ingestion()

for payload in payloads:
    ingestion.process(payload=payload)
