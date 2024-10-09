from src.api_work import HH, Avito, SuperJob
from src.utils import selection_service, selection_saver, work_on_file, sort_vacancyes, get_vacancy_by_word
from src.vacancy import Vacancy
from src.saver import JSONSaver


def main():
    """Запуск программы"""

    print("Здравствуйте! Это программа для работы с ваккансиями на сайтах по подбору персонала.\n")
    service = selection_service()  # выбор сервиса для поиска
    file_saver = selection_saver()  # выбор формата файла для сохранения

    if service == 1:
        user_keyword = input("Введите назвние профессии для поиска: ").lower()  # название професси для поиска
        user_page = int(input("Ввыберите колличество страниц для отображения: "))  # количество страниц для отображения
        hh_vacancy = HH()
        list_vacancy = hh_vacancy.load_vacancies(user_keyword, user_page)
        if file_saver == 1:
            file_ = JSONSaver("vacancyes")
            file_.delete_vacancy()
            for one_vacancy in list_vacancy:
                vacancy = Vacancy.list_hh(one_vacancy)
                dict_vacancy = vacancy.to_dict()
                file_.add_vacancy(dict_vacancy)

            print("Список вакансиий составлен!")

            work = work_on_file()
            data = file_.get_vacancy()
            if work == 1:
                for i in data:
                    vacancy = Vacancy.list_hh(i)
                    print(vacancy)
            elif work == 2:
                sort_data = sort_vacancyes(data)
                for i in sort_data:
                    vacancy = Vacancy.list_hh(i)
                    print(vacancy)
            elif work == 3:
                get_by_word = get_vacancy_by_word(data)
                for i in get_by_word:
                    vacancy = Vacancy.list_hh(i)
                    print(vacancy)
            elif work == 4:
                file_.delete_vacancy()
                print("Файл очищен!")
            elif work == 5:
                print("Спасибо. До новых встреч!")


    elif service == 2:
        avito_vacancy = Avito()
        pass
    elif service == 3:
        super_job_vacancy = SuperJob()
        pass


if __name__ == '__main__':
    main()