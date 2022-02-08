from owlready2 import *
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class HumanState(Thing):
    label = 'Human State'


dcterms.description[HumanState] = """
A human state is the particular condition that someone is in at a specific time. Human states range from simple physiological states as feeling full / hungry to complex cognitive constructs, such as feeling successful in one’s chosen career.
"""


class ClientState(HumanState):
    label = 'Client State'
    is_a = [
        compass.hasTimeScale.only(str),
        compass.hasStartDate.only(time.DateTimeDescription),
        compass.hasEndDate.only(time.DateTimeDescription),
        cids.hasCode.only(cids.Code)
    ]


ClientState.is_a.append(compass.isBarrierFor.only(ClientState))
dcterms.description[ClientState] = """
Client states are human states that are relevant to the practice of Social Work. 
"""


class DesiredClientState(ClientState):
    label = 'Desired Client State'
    pass


dcterms.description[DesiredClientState] = """
We assume that humans prefer to be in certain states, their desired states, which, depending on the community of practice, can be divided into various core categories, e.g., survival/existence, welfare, interpersonal relatedness, flourishing. There is no consensus in the field, and many different categorizations exist.
"""


class ActualClientState(ClientState):
    label = 'Actual Client State'
    pass


class CurrentClientState(ClientState):
    label = 'Current Client State'
    pass
