from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def products_stocked_by_company(invetory):
        counter = Counter(
            product["nome_da_empresa"] for product in invetory
        ).most_common()

        report = ""
        for company, count in counter:
            report += f"- {company}: {count}\n"

        return report

    @classmethod
    def generate(cls, inventory):
        older_manufacturing_date = cls.get_older_manufacturing_date(inventory)
        nearest_expiration_date = cls.get_nearest_expiration_date(inventory)
        company_with_more_products = cls.get_company_with_more_products(
            inventory
        )
        products_stocked_by_company = cls.products_stocked_by_company(
            inventory
        )

        return (
            f"Data de fabricação mais antiga: {older_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}\n"
            "Produtos estocados por empresa:\n"
            f"{products_stocked_by_company}"
        )
