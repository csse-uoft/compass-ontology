from owlready2 import *
from src.namespaces import compass, cids, time, dcterms


class ClientStatus(Thing):
    label = 'Client Status'
    from .client_state import ClientState
    from .event import Event
    is_a = [
        # compass.inducesClientState.only(ClientState),
        # compass.hasStartDate.only(time.DateTimeDescription),
        # compass.hasEndDate.only(time.DateTimeDescription),
        # compass.inducedByEvent.only(Event),
        cids.hasCode.only(cids.Code)
    ]


dcterms.description[ClientStatus] = """
We define a client’s status as their standing or position (relative to that of others) in the eyes of the law or some other form of recognized authority, such as immigration status as recognized by a country’s government, disability status as recognized by disability associations, service provider agencies, and various levels of government.
"""
