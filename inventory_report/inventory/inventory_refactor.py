from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = list()

    def import_data(self, filepath, type):
        self.data.extend(self.importer.import_data(filepath))
        if type == "simples":
            return SimpleReport.generate(self.data)
        elif type == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
