from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    def __init__(self, input_str: str, args: List[str]):
        self.input_str = input_str
        self.args = args

    @abstractmethod
    def execute(self):
        """
        execute user input
        :return:
        """
        pass
