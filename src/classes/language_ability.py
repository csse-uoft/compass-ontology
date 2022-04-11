from owlready2 import *
from src.namespaces import compass, cids, schema, xsd, dcterms
from src.utils import get_class


class LanguageAbility(Thing):
    label = 'Language Ability'
    is_a = [
        schema.knowsLanguage.exactly(1, get_class('CL-Languages')),
        compass.hasProficiency.exactly(1, get_class('CL-LanguageProficiency')),
        compass.birthLanguage.exactly(1, bool),
        compass.homeLanguage.exactly(1, bool),
    ]


dcterms.description[LanguageAbility] = """
LanguageAbility class specifies for each language, the client’s proficiency and whether it is a birth and/or home language.

•	knowsLanguage: defines the language being described.
•	hasProficiency: level of proficiency the client has for the language, eg., {native, fluent, …}.
•	birthLanguage: True if this was the language at birth.
•	homeLanguage: True if this is the language used at home.
"""
