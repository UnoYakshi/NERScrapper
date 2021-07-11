import re


def extract_phone_numbers(string: str):
    # r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    # r = re.compile(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}')
    r = re.compile(r'^[\+]?[\d]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$ ')

    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
