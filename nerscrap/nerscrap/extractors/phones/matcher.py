from spacy.matcher import Matcher
from .ner import nlp


phone_pattern = [[{'SHAPE': 'dd', 'OP': '?'}, {'ORTH': '('}, {'SHAPE': 'ddd'}, {'ORTH': ')'}, {'SHAPE': 'dddd'}, {'ORTH': '-', 'OP': '?'}, {'SHAPE': 'dddd'}]]
matcher = Matcher(nlp.vocab)
matcher.add("PhoneNumber", phone_pattern)
