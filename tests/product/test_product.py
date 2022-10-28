from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "2022-10-28",
        "2024-10-28",
        "123456",
        "instrucoes_de_armazenamento",
    )
    assert product.id == 1
    assert product.nome_do_produto == "nome_do_produto"
    assert product.nome_da_empresa == "nome_da_empresa"
    assert product.data_de_fabricacao == "2022-10-28"
    assert product.data_de_validade == "2024-10-28"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "instrucoes_de_armazenamento"
