def selection_service() -> int:
    """
    Функция для оперделения сервиса по подбору персонала
    return: код (цифра) выбранного сервиса
    """

    massege_service = ("\nВыберите сервис по подбору персонала: \n"
                       "Веедите '1' если хотите ислользовать 'HeadHunter' \n"
                       "Веедите '2' если хотите ислользовать 'Авито' \n"
                       "Веедите '3' если хотите ислользовать 'SuperJob'\n"
                       )
    while True:
        print(massege_service)
        try:
            user_service = int(input("После ввода нажмите Enter: "))
        except ValueError:
            print("ВВЕДИТЕ ЧИЛОВОЕ ЗНАЧЕНИЕ!")
            selection_service()
        else:
            if user_service in [1, 2, 3]:
                break
            print("ВВЕДЕН НЕВЕРНЫЙ КОД!")

    return user_service


def selection_saver():
    """
    Функция для определения формата рабочегно файла
    return: код (цифра) выбранного файла для работы
    """

    massege = ("\nВыберите в каком формате хотите хранить данные?: \n"
               "Веедите '1' если хотите ислользовать JSON \n"
               "Веедите '2' если хотите ислользовать EXCEL \n"
               "Веедите '3' если хотите ислользовать SCV \n"
               "Веедите '4' если хотите ислользовать TXT \n"
               )
    while True:
        print(massege)
        try:
            user_saver = int(input("После ввода нажмите Enter: "))
        except ValueError:
            print("ВВЕДИТЕ ЧИЛОВОЕ ЗНАЧЕНИЕ!")
            selection_saver()
        else:
            if user_saver in [1, 2, 3, 4]:
                break
            print("ВВЕДЕН НЕВЕРНЫЙ КОД!")

    return user_saver


def work_on_file():
    """
    Функция для определения формы работы с файлом
    return: код (цифра) выбранной формы работы с файлом
    """

    massege = ("\nВыберите дальнейшие действия : \n"
               "Веедите '1' если хотите вывести все вакансии \n"
               "Веедите '2' если хотите выбрать топ вакансий по зарплате \n"
               "Веедите '3' если хотите получить вакансии с ключевым словом в описании \n"
               "Веедите '4' если хотите очистить файл \n"
               "Веедите '5' Выход из рограммы \n"
               )
    while True:
        print(massege)
        try:
            user_work = int(input("После ввода нажмите Enter: "))
        except ValueError:
            print("ВВЕДИТЕ ЧИЛОВОЕ ЗНАЧЕНИЕ!")
            work_on_file()
        else:
            if user_work in [1, 2, 3, 4, 5]:
                break
            print("ВВЕДЕН НЕВЕРНЫЙ КОД!")

    return user_work


def sort_vacancyes(vacancyes: list[dict]):
    """
    Функция сортирует вакансии по зарплате в порядке убывания
    :param vacancyes: список словарей вакансий
    :return: топ вакансий (колличество выбирается пользователем)
    """
    quantity = int(input("Введите колличество топ вакансий:\n"))
    sorted_vacancyes = sorted(vacancyes, key=lambda x: x["salary"]["from"], reverse=True)

    return sorted_vacancyes[:quantity]


def get_vacancy_by_word(vacancyes: list[dict]):
    """
    Функция фильтрует выкансии по слову в описании
    :param vacancyes:
    :return:список выкансий по ключевому слову в описании
    """
    user_keyword = input("Введите ключевое слово для поиска вакансий:\n").lower()
    filtr_vacancyes = []
    for vacancy in vacancyes:
        requirement = str(vacancy["snippet"]["requirement"])
        responsibility = str(vacancy["snippet"]["responsibility"])
        if user_keyword in requirement.lower() or user_keyword in responsibility.lower():
            filtr_vacancyes.append(vacancy)

    return filtr_vacancyes
