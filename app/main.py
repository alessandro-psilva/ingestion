import os
import json
from module.ingestion import Ingestion


def main():
    path_app = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(path_app, "ingestion", "app", "data", "payloads.json")    

    with open(file_path, "r") as file:
        payloads = json.load(file)

    ingestion = Ingestion()

    for payload in payloads:
        ingestion.process(payload=payload)


if __name__ == '__main__':
    main()
