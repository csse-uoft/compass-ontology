from owlready2 import *
from src.namespaces import compass, cids, time, dcterms
from src.utils import get_class


class ClientGoal(Thing):
    label = 'Client Goal'
    is_a = [
        compass.inducesNeed.only(get_class('ClientNeed')),
        compass.hasDeadline.only(time.DateTimeDescription),
        compass.hasTemporalHorizon.only(str)
    ]


ClientGoal.is_a.append(compass.hasSubGoal.only(ClientGoal))
dcterms.description[ClientGoal] = """
A client goal can consist of several sub-goals whose fulfillment would contribute to meeting the overarching goal. (Instances of type Client Goal can be linked to other ClientGoal instances via hasSubGoal.) Client goals reveal the underlying client needs. (Property inducesClientNeed links instances of type ClientNeed to the specific client goal they are related to.) 
"""