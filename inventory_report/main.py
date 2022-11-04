import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _, filepath, report_type = sys.argv

    if filepath.endswith(".csv"):
        return sys.stdout.write(
            InventoryRefactor(CsvImporter).import_data(filepath, report_type)
        )

    if filepath.endswith(".json"):
        return sys.stdout.write(
            InventoryRefactor(JsonImporter).import_data(filepath, report_type)
        )

    if filepath.endswith(".xml"):
        return sys.stdout.write(
            InventoryRefactor(XmlImporter).import_data(filepath, report_type)
        )
