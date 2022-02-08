from owlready2 import Thing
from src.namespaces import compass, cids, time, oep, dcterms
from src.utils import get_class


class ClientOutcome(cids.StakeholderOutcome):
    label = 'Client Outcome'
    is_a = [
        oep.partOf.only(get_class('ServiceOutcome'))
    ]

dcterms.description[ClientOutcome] = """
Client outcomes reflect the success of a social intervention / provision of service and are directly related to the expressed/assessed client needs via the changes in the client state effected via the need satisfiers provided by the services the client received. 

Client outcomes are also related to service outcomes and service goals (which include outcomes and goals for all stakeholders, not just their clients). For example:
•	a client’s successful integration into their chosen community contributes to achieving the goal of integrating all newcomers into that community
•	a minor client’s successful rehabilitation and preservation of family support contributes to the reduction in fostering for the client’s home community / region
•	a client’s improved employment status contributes to the reduction of under-employment among immigrants in the client’s home community / region.
"""