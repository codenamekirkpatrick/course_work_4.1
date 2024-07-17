import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Python-разработчик", "https://hh.ru/vacancy/00000",
                   5_000_000, 10_000_000, "Москва",
                   "Опыт работы обязателен", "Разарботка программ")


@pytest.fixture()
def vacancy2():
    return Vacancy("Python-разработчик", "https://hh.ru/vacancy/00000",
                   50_000, 100_000, "Ташкент",
                   "Опыт работы обязателен", "Разарботка программ")