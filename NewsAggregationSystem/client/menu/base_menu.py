from abc import ABC, abstractmethod

class BaseMenu(ABC):

    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def api_request(self):
        pass
