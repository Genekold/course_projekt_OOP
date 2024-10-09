class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, id, name, salary_from, salary_to, url_vac, requirement, responsibility, address=None):
        """Конструктор класса"""
        self.__id = id
        self.__name = name
        self.__salary_from = self.__valid_salary(salary_from)
        self.__salary_to = self.__valid_salary(salary_to)
        self.url_vac = url_vac
        self.requirement = requirement
        self.responsibility = responsibility
        self.address = address

    def __valid_salary(self, salary: int | None) -> int:
        """Ваидация данных"""

        return salary if salary else 0

    def __str__(self) -> str:
        """Строковое представление вакакнсии"""

        return (
            f"id: {self.__id}\n"
            f"Наименование вакансии: {self.__name}\n"
            f"Заработная плата: от {self.__salary_from} до {self.__salary_to}\n"
            f"Ссылка на вкансию: {self.url_vac}\n"
            f"Требования к профессии: {self.requirement}\n"
            f"Обязанности: {self.responsibility}\n"
            f"Место работы: {self.address}"
        )

    def __lt__(self, other) -> bool:
        """Метод сравнения экземпляров"""

        salery_self = [self.__salary_from, self.__salary_to]
        salery_other = [other.__salery_from, other.__salary_to]
        return salery_self < salery_other

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в виде словаря"""

        return {
            "id": self.__id,
            "name": self.__name,
            "salary": {
                "from": self.__salary_from,
                "to": self.__salary_to,
            },
            "alternate_url": self.url_vac,
            "snippet": {
                "requirement": self.requirement,
                "responsibility": self.responsibility,
            },
            "address": self.address,
        }

    @classmethod
    def list_hh(cls, data_vacancy: dict):
        """Метод возвращает экземпляр класса в виде списка"""

        return cls(
            data_vacancy["id"],
            data_vacancy["name"],
            data_vacancy["salary"]["from"],
            data_vacancy["salary"]["to"],
            data_vacancy["alternate_url"],
            data_vacancy["snippet"]["requirement"],
            data_vacancy["snippet"]["responsibility"],
            data_vacancy["address"],
        )
