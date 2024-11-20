def test_add_vacancy(json_saver):
    json_saver.add_vacancy({'id': '107292263', 'name': 'Заместитель главного механика по автотранспорту'})
    assert len(json_saver.get_vacancy()) == 1


def test_get_vacancy(json_saver):
    """Тест проверяет что находится в тестовом файле"""
    assert json_saver.get_vacancy() == [{'id': '107292263', 'name': 'Заместитель главного механика по автотранспорту'}]


def test_json_saver_del(json_saver):
    """Тест проверяет очистку файла"""
    assert json_saver.delete_vacancy() is None
