from abc import ABC, abstractmethod


class ExternalServerService(ABC):

    @abstractmethod
    def fetch_the_news_articles(self, server_config):
        pass
