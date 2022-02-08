from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization
from src.utils import get_class


class Gender(Thing):
    is_a = [
        cids.hasDescription.only(str),
        cids.hasCode.exactly(1, cids.Code)
    ]


class Sex(Thing):
    is_a = [
        cids.hasDescription.only(str),
        cids.hasCode.exactly(1, cids.Code)
    ]