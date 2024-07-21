import requests
from src.get_vacancies import GetVacanciesAPI
from src.vacancy import Vacancy


class HeadHunterAPI(GetVacanciesAPI):
    """ Класс для подключения к hh.ru """

    def __init__(self):
        """Конструктор класса"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies = []

    def get_response(self, keyword, per_page):
        """Метод запроса вакансий"""
        params = {"text": keyword, "per_page": per_page}
        return requests.get(self.url, params=params)

    def get_vacancies(self, keyword, per_page):
        """Метод получения вакансий"""
        return self.get_response(keyword, per_page).json()["items"]

    def get_filter_vacancies(self, keyword, per_page):
        """Метод фильтрации вакансий"""
        filter_vacancies = []
        vacancies = self.get_vacancies(keyword, per_page)
        for vacancy in vacancies:
            filter_vacancies.append(Vacancy.vacancies_lst(vacancy))
        return filter_vacancies