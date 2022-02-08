from owlready2 import *
from src.namespaces import compass, cids, time, dcterms


class ClientProblem(Thing):
    label = 'Client Problem'
    from .client_goal import ClientGoal
    from .client_state import ClientState
    is_a = [
        compass.inducesGoal.only(ClientGoal),
        compass.hasActualClientState.only(ClientState),
        compass.hasDesiredClientState.only(ClientState),
        compass.hasStartDate.only(time.DateTimeDescription),
        compass.hasEndDate.only(time.DateTimeDescription)
    ]


# dcterms.description[ClientProblem] = """
# """