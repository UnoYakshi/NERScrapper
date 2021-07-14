from typing import List

import spacy

from extractors.phones.abs import PhoneExtractor


nlp = spacy.load('en_core_web_sm')


class NERPhonesExtractor(PhoneExtractor):
    def __init__(self):
        ...

    @staticmethod
    def recognize_phones(text: str) -> List[str]:
        doc = nlp(text)
        # phones = matcher(doc)
        phones = [entity for entity in doc.ents if entity.label_ == 'PHONE']
        return phones
