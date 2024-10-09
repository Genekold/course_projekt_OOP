import json
import os.path
from abc import ABC, abstractmethod

from config import DATA_DIR


class Saver(ABC):
    """Абстрактный класс для записи в файл"""

    def __init__(self, filename: str):
        self.filname = filename

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Saver):
    """Класс для записи в JSON-файл"""

    def __init__(self, filename: str):
        """Конструктор класса"""
        super().__init__(filename)
        self.path_file = os.path.join(DATA_DIR, self.filname + ".json")

    def get_vacancy(self):
        """Получение данных из JSON-файла"""

        try:
            with open(self.path_file, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []

        return data

    def add_vacancy(self, vacancy: dict):
        """Запись даннх в JSON-файл"""

        data = self.get_vacancy()
        data.extend([vacancy])
