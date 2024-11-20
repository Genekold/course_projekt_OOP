def test_vacancies_init(vac_1):
    assert vac_1.url_vac == "https://hh.ru/vacancy/106393343"
    assert vac_1.requirement == 'Наличие всех категорий (B,C,D,E).'
    assert vac_1.responsibility == "Перевозка работников и строительных материалов."
    assert vac_1.address == "Москва"


def test_vacancies_lt(vac_1, vac_2):
    assert vac_1 < vac_2


def test_vacancies_to_dict(vac_1):
    assert vac_1.to_dict() == {
        "id": 123456,
        "name": "Водитель автомобиля",
        'salary': {
            "from": 20000,
            "to": 0,
        },
        "alternate_url": "https://hh.ru/vacancy/106393343",
        "snippet": {
            "requirement": 'Наличие всех категорий (B,C,D,E).',
            "responsibility": "Перевозка работников и строительных материалов."
        },
        "address": "Москва"
    }
