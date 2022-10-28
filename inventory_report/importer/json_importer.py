import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(filepath, "r") as file:
            return json.load(file)
