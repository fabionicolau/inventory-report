from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "123456",
        "ao abrigo de luz",
    )
    assert product.__repr__() == (
        "O produto farinha fabricado em 01-05-2021 por Farinini com validade"
        + " até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    )
