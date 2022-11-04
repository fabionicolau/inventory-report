from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


data_mock = [
    {
        "nome_do_produto": "Coca-Cola",
        "nome_da_empresa": "Coca-Cola Company",
        "data_de_fabricacao": "2020-01-01",
        "data_de_validade": "2022-11-02",
        "numero_de_serie": "123456789",
        "instrucoes_de_armazenamento": "Manter em local seco",
    },
    {
        "nome_do_produto": "Sprite",
        "nome_da_empresa": "Coca-Cola Company",
        "data_de_fabricacao": "2020-04-01",
        "data_de_validade": "2023-12-01",
        "numero_de_serie": "1212312d6789",
        "instrucoes_de_armazenamento": "Manter em local seco",
    },
    {
        "nome_do_produto": "Pepsi",
        "nome_da_empresa": "Pepsico",
        "data_de_fabricacao": "2020-04-01",
        "data_de_validade": "2024-01-01",
        "numero_de_serie": "1232389",
        "instrucoes_de_armazenamento": "Manter em local seco",
    },
]


def test_decorar_relatorio():
    report_mock = (
        "\033[32mData de fabricação mais antiga:\033[0m"
        + " \033[36m2020-01-01\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        + " \033[36m2023-12-01\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        + " \033[31mCoca-Cola Company\033[0m"
    )

    report = ColoredReport(SimpleReport).generate(data_mock)

    assert report == report_mock
