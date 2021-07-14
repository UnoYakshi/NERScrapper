import re
from typing import List

from extractors.phones.abs import PhoneExtractor

# r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
# r = re.compile(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}')
# r = re.compile(r'^[\+]?[\d]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$ ')
r = re.compile(r'([+]?[78]+[( ]?[0-9]{3}[) ]?[\s.-]?[0-9]{7})')


class RegexPhonesExtractor(PhoneExtractor):
    def __init__(self):
        ...

    @staticmethod
    def extract_phones(text: str) -> List[str]:
        phone_numbers = r.findall(text)
        return [re.sub(r'\D', '', number) for number in phone_numbers]
