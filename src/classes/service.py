from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms
from src.utils import get_class


class Service(cids.Service):
    label = 'Service'
    is_a = [
        compass.hasRequirement.only(cids.Characteristic),
        compass.hasFocus.only(cids.Characteristic),
        compass.hasMode.only(compass['CL-ServiceMode']),
        compass.providesSatisfier.only(get_class('NeedSatisfier')),

        compass.providedBy.min(1),
        # compass.hasCost.max(1),
    ]


dcterms.description[Service] = """
The Compass Service class is an extension of the cids:Service class.

• hasRequirement: Identifies characteristics that limit who can use the service, listed in Client taxonomy code list.
• hasFocus: Identifies client characteristics that the service focuses on, listed in Client taxonomy code list.
• hasMode: The mode with which the service is delivered.
• providesSatisfier: The need satisfier this service provides.
• providedBy: The organization provides this service.
"""


class Application(Service):
    label = 'Application'
    is_a = [
        compass.hasSource.only(str)
    ]

dcterms.description[Application] = """
Clients can interact with service providers through a computer application, a subclass of cids:Service. An Application has the following property:
•	hasSource: The URL or unique address where the application can be referenced.
"""


class Referral(Thing):
    label = 'Referral'
    pass


class ServiceBarrier(Thing):
    label = 'Service Barrier'
    pass
