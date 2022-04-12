from owlready2 import *
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class ClientGoal(Thing):
    label = 'Client Goal'
    is_a = [
        compass.inducesNeed.only(get_class('ClientNeed')),
        # compass.hasDeadline.only(time.DateTimeDescription),
        # compass.hasTemporalHorizon.only(str)
        compass.inducesNeed.only(get_class('Need')),
        compass.hasTimeHorizon.exactly(1, str),
        cids.hasCode.only(cids.Code)
    ]


ClientGoal.is_a.append(compass.hasSubGoal.only(ClientGoal))
dcterms.description[ClientGoal] = """
A client goal is a cognitive representation that includes a (desired) client state that one must deploy various means to make happen, and/or maintain, and a time horizon for achieving/maintaining it.

• inducesNeed: links to instances of type Need that specify the client needs induced by the goal
• hasTimeHorizon: specifies the timescale of the goal, e.g., short-term, long-term
• hasSubGoal: links to instances of type Goal that specify subgoals
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of client goal.
"""