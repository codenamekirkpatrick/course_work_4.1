from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    """Абстрактный класс для получения вакансии с hh.ru"""

    @abstractmethod
    def get_response(self, keyword, per_page): # получение ответа
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page): # получение вакансий
        pass

    @abstractmethod
    def get_filter_vacancies(self, keyword, per_page): # получение фильтра
        pass