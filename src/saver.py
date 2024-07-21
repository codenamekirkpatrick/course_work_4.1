from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс для получения и записи вакансии с сайта hh.ru"""
    @abstractmethod
    def write_data(self):
        """Абстрактный метод записи информации"""
        pass

    @abstractmethod
    def get_data(self):
        """Абстрактный метод получения информации"""
        pass

    @abstractmethod
    def del_data(self, data_json):
        """Абстрактный метод удаления информации"""
        pass