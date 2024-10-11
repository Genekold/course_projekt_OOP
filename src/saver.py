import os.path
from abc import ABC, abstractmethod
import json

from config import DATA_DIR


class Saver(ABC):
    """Абстрактный класс для записи в файл"""

    def __init__(self):
        pass

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

    def __init__(self, filename: str = "vacancies"):
        """Конструктор класса"""
        self.__filename = filename
        self.path_file = os.path.join(DATA_DIR, self.__filename + ".json")

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

        with open(self.path_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self):
        """Удаление данных из JSON-файла"""

        with open(self.path_file, "w", encoding="utf-8") as file:
            json.dump([], file)


class EXCELSaver(Saver):
    """Класс для записи в EXCEL-файл"""
    pass


class CSVSaver(Saver):
    """Класс для записи в CSV-файл"""
    pass


class TXTSaver(Saver):
    """Класс для записи в TXT-файл"""
    pass
