from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "123456",
        "ao abrigo de luz",
    )
    assert product.id == 1
    assert product.nome_do_produto == "farinha"
    assert product.nome_da_empresa == "Farinini"
    assert product.data_de_fabricacao == "01-05-2021"
    assert product.data_de_validade == "02-06-2023"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "ao abrigo de luz"
