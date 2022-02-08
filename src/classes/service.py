from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms
from src.utils import get_class


class Service(cids.Service):
    label = 'Service'
    is_a = [
        compass.providedBy.min(1),
        compass.providesSatisfier.only(get_class('NeedSatisfier')),
        compass.hasCost.max(1)
    ]


dcterms.description[Service] = """
A Program is composed of one or more Services.  For example, a poverty reduction program can have many services with each service comprised of different activities, Inputs, Outputs and Outcomes. For the Compass service pattern, we extend the CIDS Service class with a property “providesSatisfier” for the need satisfier the service provides.

•	act:hasSubActivity: Identifies the Activities that comprise the Service.
•	hasInput: Identifies the Inputs to the Service.
•	hasOutput: Identifies the Outputs of the Service.
•	hasOutcome: Identifies the Outcomes that are specific to the Service.
•	hasContributingStakeholder: Identifies the stakeholders that contribute to the Service.
•	hasBeneficialStakeholder: Identifies the stakeholders that benefit from the Service.
•	beneficiarySizeStart: Number of beneficial stakeholders at the beginning of the service time interval.
•	beneficiarySizeEnd: Number of beneficial stakeholders at the end of the service time interval.
•	time:hasTime: Time interval over which the service is provided.
•	providesSatisfier: The satisfier this service provides.
•	providedBy: The organization provides this service.
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
