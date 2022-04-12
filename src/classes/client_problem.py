from owlready2 import *
from src.namespaces import compass, cids, time, dcterms


class ClientProblem(Thing):
    label = 'Client Problem'
    from .client_goal import ClientGoal
    # from .client_state import ClientState
    is_a = [
        compass.inducesGoal.only(ClientGoal),
        # compass.hasActualClientState.only(ClientState),
        # compass.hasDesiredClientState.only(ClientState),
        compass.hasStartDate.only(time.DateTimeDescription),
        compass.hasEndDate.only(time.DateTimeDescription),
        cids.hasCode.only(cids.Code),
    ]


dcterms.description[ClientProblem] = """
A client problem is a cognitive representation of the discrepancy between an actual client state and a desired client state.

• inducesGoal links to instances of type ClientGoal that specify the goals induced by the problem.
• hasStartClientState links to instances of type ClientState that specify the actual state the client is in at the time the problem is identified
• hasEndClientState links to instances of type ClientState  that specify the desired state of the client at the time the problem is identified
• hasCode: specifies zero or more codes, created by various organizations, to identify a type of client  problem
"""