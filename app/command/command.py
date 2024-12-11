from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    def __init__(self, args: List[str]):
        self.args = args

    @abstractmethod
    def execute(self):
        """
        execute user input
        :return:
        """
        pass
