import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для выполнения запросов с сервисов по поиску работы"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword, page):
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'text': '',
            'page': 0,
            'per_page': 100,
            'currency': 'RUR',
            'only_with_salary': True,
            'area': 113
        }
        self.vacancies = []

    def load_vacancies(self, keyword, page):
        self.params['text'] = keyword
        for i in range(page):
            response = requests.get(self.__url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.params['page'] += 1
            self.vacancies.extend(vacancies)

        return self.vacancies


class Avito(Parser):
    """Класс для работы с API Avito"""
    pass


class SuperJob(Parser):
    """Класс для работы с API SuperJob"""
    pass
