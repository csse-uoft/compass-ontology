from owlready2 import Thing
from src.namespaces import compass, cids, time, oep, dcterms
from src.utils import get_class


class ClientOutcome(cids.StakeholderOutcome):
    label = 'Client Outcome'
    is_a = [
        oep.partOf.only(get_class('ServiceOutcome')),
        cids.hasCode.only(cids.Code),
    ]

dcterms.description[ClientOutcome] = """
Client outcome is a change in a set of client features, e.g., improved proficiency in English, improved life skills, improved nutrition, improved housing conditions, improved chances of recovery from alcohol adiction.

• partOf: links to instances of more complex Outcome that this outcome is a part of.
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of client outcome.
"""