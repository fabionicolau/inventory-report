from datetime import datetime
from collections import Counter


class SimpleReport:
    def get_older_manufacturing_date(inventory):
        return min(product["data_de_fabricacao"] for product in inventory)

    def get_nearest_expiration_date(inventory):
        today = datetime.today()

        return min(
            [
                product["data_de_validade"]
                for product in inventory
                if datetime.fromisoformat(product["data_de_validade"]) >= today
            ]
        )

    def get_company_with_more_products(inventory):
        return Counter(
            product["nome_da_empresa"] for product in inventory
        ).most_common(1)[0][0]

    @classmethod
    def generate(cls, inventory):
        older_manufacturing_date = cls.get_older_manufacturing_date(inventory)
        nearest_expiration_date = cls.get_nearest_expiration_date(inventory)
        company_with_more_products = cls.get_company_with_more_products(
            inventory
        )

        return (
            f"Data de fabricação mais antiga: {older_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
