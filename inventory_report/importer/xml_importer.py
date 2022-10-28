import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filepath):
        if not filepath.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(filepath, "r") as file:
            reader = xmltodict.parse(file.read())
            return reader["dataset"]["record"]
