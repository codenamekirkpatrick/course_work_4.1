from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с сайта hh.ru"""

    @abstractmethod
    def get_response(self, keyword, per_page):
        """Абстрактный метод для получения ответа"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        """Абстрактный метод для получения вакансии"""
        pass

    @abstractmethod
    def get_filter_vacancies(self, keyword, per_page):
        """Абстрактный метод для получения вакансии исходя из запроса"""
        pass