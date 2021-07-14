from abc import abstractmethod, ABCMeta
from typing import List


class PhoneExtractor(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def extract_phones(text: str) -> List[str]:
        raise NotImplemented
