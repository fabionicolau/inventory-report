from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

import csv
import json
import xmltodict


class Inventory:
    def csv_reader(filepath):
        with open(filepath, "r") as file:
            reader = list(csv.DictReader(file))
            return reader

    def json_reader(filepath):
        with open(filepath, "r") as file:
            reader = json.load(file)
            return reader

    def xml_reader(filepath):
        with open(filepath, "r") as file:
            reader = xmltodict.parse(file.read())
            return reader["dataset"]["record"]

    @classmethod
    def data_reader(cls, filepath):
        if filepath.endswith(".csv"):
            return cls.csv_reader(filepath)
        elif filepath.endswith(".json"):
            return cls.json_reader(filepath)
        elif filepath.endswith(".xml"):
            return cls.xml_reader(filepath)

    @classmethod
    def import_data(cls, filepath, type):
        data = cls.data_reader(filepath)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
