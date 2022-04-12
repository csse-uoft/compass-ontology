from owlready2 import *
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class PersonState(Thing):
    label = 'Person State'


dcterms.description[PersonState] = """
A person state is the particular condition that someone is in at a specific time. Human states range from simple physiological states as feeling full / hungry to complex cognitive constructs, such as feeling successful in one’s chosen career.
"""


class ClientState(PersonState):
    label = 'Client State'
    is_a = [
        compass.hasTimeScale.only(str),
        # compass.hasStartDate.only(time.DateTimeDescription),
        # compass.hasEndDate.only(time.DateTimeDescription),
        cids.hasCode.only(cids.Code)
    ]


ClientState.is_a.append(compass.isBarrierFor.only(ClientState))
dcterms.description[ClientState] = """
ClientState: a person’s condition with respect to circumstances, often, but not necessarily durable or lasting, e.g., is homeless, feels anxious, feels depressed, lacks basic life skills, etc..

• isBarrierFor links to instances of type ClientState that specify the other states that could be adversely affected by this state.
• hasTimeScale: specifies the timescale of the state, e.g., “acute”, “chronic”, “short-term”, “long-term”, medium-term”.
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of state for the client.

"""


class DesiredState(ClientState):
    label = 'Desired Client State'
    pass


dcterms.description[DesiredState] = """
DesiredClientState: a person’s desired condition, e.g.,  “(being) adequately fed”, “(living) in a safe, supportive environment”, “(being) in a good mental health state” 
"""


class ActualState(ClientState):
    label = 'Actual Client State'
    pass


dcterms.description[ActualState] = """
ActualClientState: a person’s current condition, e.g.,  “feeling hungry”, “(living) in an unsafe environment”, “(feeling) depressed”
"""

# class CurrentClientState(ClientState):
#     label = 'Current Client State'
#     pass
