import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def vac_1():
    return Vacancy(
        123456,
        'Водитель автомобиля',
        20000,
        None,
        'https://hh.ru/vacancy/106393343',
        'Наличие всех категорий (B,C,D,E).',
        "Перевозка работников и строительных материалов.",
        "Москва"
    )


@pytest.fixture()
def vac_2():
    return Vacancy(
        543232,
        'Машинист мостового крана',
        70000,
        300000,
        'https://hh.ru/vacancy/106393343',
        'Наличие удостоверени ',
        "Перевозка работников и строительных материалов.",
        "Красноярск, Башиловская улица, 8"
    )
