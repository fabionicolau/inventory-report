import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
