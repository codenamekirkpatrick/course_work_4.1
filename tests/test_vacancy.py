

def test_vacancy_init(vacancy):
    """ Тесты конструктора класса """

    assert vacancy.name == "Python-разработчик"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/00000"
    assert vacancy.salary_from == 5000000
    assert vacancy.salary_to == 10000000
    assert vacancy.area_name == "Москва"
    assert vacancy.requirement == "Опыт работы обязателен"
    assert vacancy.responsibility == "Разарботка программ"



def test_vacancy_str(vacancy):
    """ Тест строкового представления вакансии """

    assert str(vacancy) == ("Наименование вакансии: Python-разработчик,\n"
                            "Ссылка на вакансию: https://hh.ru/vacancy/00000,\n"
                            "Зарплата: от 5000000 до 10000000,\n"
                            "Место работы: Москва,\n"
                            "Краткое описание: Опыт работы обязателен,\n"
                            "Разарботка программ\n")



def test_vacancy_lt(vacancy, vacancy2):
    """ Тест утверждает, что одно значение меньше другого """

    assert vacancy > vacancy2
    if vacancy < vacancy2:
        assert ValueError