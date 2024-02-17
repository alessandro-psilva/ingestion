import json
from module.ingestion import Ingestion


if __name__ == '__main__':
    with open("app/data/payloads.json", "r") as arq:
        payloads = json.load(arq)

    ingestion = Ingestion()

    for payload in payloads:
        ingestion.process(payload=payload)
