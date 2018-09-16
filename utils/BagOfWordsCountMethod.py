from abc import ABC, abstractmethod


class CountMethod(ABC):
    @abstractmethod
    def count(self, text):
        pass
