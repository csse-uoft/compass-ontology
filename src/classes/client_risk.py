from owlready2 import Thing
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class RiskFactor(Thing):
    label = 'Risk Factor'
    is_a = [
        compass.hasType.only(str),
        cids.hasCode.only(cids.Code),
        # compass.affectsRisk.only(get_class('Risk')),
        # compass.hasStartDate.only(time.DateTimeDescription),
        # compass.hasEndDate.only(time.DateTimeDescription)
    ]


dcterms.description[RiskFactor] = """
A risk factor is something that increases the risk of a person to develop or enter a condition or state, e.g. housing precarity increases a person’s risk of becoming homeless. 

• hasType: specifies the type of risk factor, e.g., a physical individual risk factor, a psychosocial individual risk factor, a person’s individual risk factor
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of risk factor.
"""

#
# class PhysicalRiskFactor(RiskFactor):
#     label = 'Physical Risk Factor'
#
#
# dcterms.description[PhysicalRiskFactor] = """
# physical individual risk factor (e.g., lack / precarity of shelter, lack / precarity of food)
# """
#
#
# class PsychosocialRiskFactor(RiskFactor):
#     label = 'Psychosocial Risk Factor'
#
#
# dcterms.description[PsychosocialRiskFactor] = """
# physical individual risk factor (e.g., lack / precarity of shelter, lack / precarity of food)
# """
#
#
# class PersonalRiskFactor(RiskFactor):
#     label = 'Personal Risk Factor'
#
#
# dcterms.description[PersonalRiskFactor] = """
# person’s individual risk factor (e.g., addicted to alcohol [health status], two detox treatments over the past 3 years [medical history], aggressive behavior [behaviour], convicted and imprisoned twice for petty theft [justice system history], etc.)
# """


class Risk(Thing):
    is_a = [
        compass.hasRiskFactor.only(RiskFactor),
        compass.inducesState.only(get_class('ClientState')),
        compass.hasType.only(str),
        compass.hasLikelihoodScore.only(str),
        cids.hasCode.only(cids.Code)
    ]


dcterms.description[Risk] = """
Risk captures the uncertainty with respect to client states, e.g., risk of being homeless, risk of being unemployed, and the risk of being a victim of sexual exploitation. (Life events materialize a client’s risks or increase/decrease its likelihood of materializing. Losing one’s job materializes the risk of being unemployed, the new client state is “is unemployed”.)

• hasRiskFactor links to instances of type RiskFactor that specify the associated risk factor
• inducesState links to instances of type ClientState that specify what client states the risk induces
• hasType specifies the type of risk, e.g.,  private, or public
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of risk.
"""


# class CommunityRisk(Risk):
#     label = 'CommunityRisk'
#
#
# class ClientRisk(Risk):
#     label = 'Client Risk'
#     is_a = [
#         compass.inducesClientState.only(get_class('ClientState')),
#         compass.inducesCommunityRisk.only(CommunityRisk)
#     ]
#
#
# dcterms.description[ClientRisk] = """
# . In our framework, a client risk describes a situation involving exposure to danger, something that may cause loss or injury, such as the risk of becoming homeless, risk of becoming unemployed, and the risk of becoming a victim of sexual exploitation.
# """
