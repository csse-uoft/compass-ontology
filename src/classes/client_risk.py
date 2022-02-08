from owlready2 import Thing
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class RiskFactor(Thing):
    label = 'Risk Factor'
    is_a = [
        compass.hasType.only(str),
        compass.affectsRisk.only(get_class('Risk')),
        compass.hasStartDate.only(time.DateTimeDescription),
        compass.hasEndDate.only(time.DateTimeDescription)
    ]


dcterms.description[RiskFactor] = """
A risk factor is something that increases the risk of a person to develop or enter a condition or state, e.g. housing precarity increases a person’s risk of becoming homeless. 
Risk factors are often divided into categories that are meaningful for a specific community of practice. For example, risk can be categorization according to its perceived source, such as physical, psychosocial or personal:
•	physical individual risk factor (e.g., lack / precarity of shelter, lack / precarity of food)
•	psychosocial individual risk factor (low social status, loneliness, helplessness, lack of work)
•	person’s individual risk factor (e.g., addicted to alcohol [health status], two detox treatments over the past 3 years [medical history], aggressive behavior [behaviour], convicted and imprisoned twice for petty theft [justice system history], etc.)
"""


class PhysicalRiskFactor(RiskFactor):
    label = 'Physical Risk Factor'


dcterms.description[PhysicalRiskFactor] = """
physical individual risk factor (e.g., lack / precarity of shelter, lack / precarity of food)
"""


class PsychosocialRiskFactor(RiskFactor):
    label = 'Psychosocial Risk Factor'


dcterms.description[PsychosocialRiskFactor] = """
physical individual risk factor (e.g., lack / precarity of shelter, lack / precarity of food)
"""


class PersonalRiskFactor(RiskFactor):
    label = 'Personal Risk Factor'


dcterms.description[PersonalRiskFactor] = """
person’s individual risk factor (e.g., addicted to alcohol [health status], two detox treatments over the past 3 years [medical history], aggressive behavior [behaviour], convicted and imprisoned twice for petty theft [justice system history], etc.)
"""


class Risk(Thing):
    is_a = [
        compass.hasRiskFactor.only(RiskFactor),
        compass.hasType.only(str),
        compass.hasLikelihoodScore.only(str),
    ]


class CommunityRisk(Risk):
    label = 'CommunityRisk'


class ClientRisk(Risk):
    label = 'Client Risk'
    is_a = [
        compass.inducesClientState.only(get_class('ClientState')),
        compass.inducesCommunityRisk.only(CommunityRisk)
    ]


dcterms.description[ClientRisk] = """
. In our framework, a client risk describes a situation involving exposure to danger, something that may cause loss or injury, such as the risk of becoming homeless, risk of becoming unemployed, and the risk of becoming a victim of sexual exploitation. 
"""
