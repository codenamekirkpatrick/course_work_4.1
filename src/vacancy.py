class Vacancy:
    """ Класс для работы с вакансиями """

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.area_name = area_name
        self.requirement = requirement
        self.responsibility = responsibility

    def __str__(self):
        return (f"Наименование вакансии: {self.name},\n"
                f"Ссылка на вакансию: {self.alternate_url},\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to},\n"
                f"Место работы: {self.area_name},\n"
                f"Краткое описание: {self.requirement},\n"
                f"{self.responsibility}\n")

    def __lt__(self, other):

        # if isinstance(self and other, int):
        return self.salary_from < other.salary_from

    @staticmethod
    def vacancies_lst(vacancy_lst):
        """ Метод возвращает вакацнию в виде списка """

        return Vacancy(
            vacancy_lst["name"],
            vacancy_lst["alternate_url"],
            vacancy_lst["salary"]["from"] if not ((vacancy_lst["salary"] is None)
                                                  or (vacancy_lst["salary"]["from"] is None)) else 0,
            vacancy_lst["salary"]["to"] if not ((vacancy_lst["salary"] is None)
                                                or (vacancy_lst["salary"]["to"] is None)) else 0,
            vacancy_lst["area"]["name"],
            vacancy_lst["snippet"]["requirement"],
            vacancy_lst["snippet"]["responsibility"],
        )

    def vacancies_dict(self):
        """ Метод возвращает вакацнию в виде словаря """

        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }