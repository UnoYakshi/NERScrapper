from typing import List

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

phone_pattern = [[{'SHAPE': 'dd', 'OP': '?'}, {'ORTH': '('}, {'SHAPE': 'ddd'}, {'ORTH': ')'}, {'SHAPE': 'dddd'}, {'ORTH': '-', 'OP': '?'}, {'SHAPE': 'dddd'}]]
matcher = Matcher(nlp.vocab)
matcher.add("PhoneNumber", phone_pattern)


def recognize_phones(text: str) -> List:
    doc = nlp(text)
    phones = matcher(doc)
    # phones = [entity for entity in doc.ents if entity.label_ == 'PHONE']
    return phones
