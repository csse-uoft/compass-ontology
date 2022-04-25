from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms, time, xsd
from src.utils import get_class


class Funding(Thing):
    label = 'Funding'
    is_a = [
        compass.receivedFrom.exactly(1, get_class('Organization', compass)),  # Specifies compass.Organization
        compass.fundersProgram.max(1, cids.Program),
        time.hasTime.only(time.DateTimeInterval),
        compass.requestedAmount.exactly(1, xsd.decimal),
        compass.receivedAmount.exactly(1, xsd.decimal),
        compass.forStakeholder.only(cids.BeneficialStakeholder),
        compass.forProgram.only(cids.Program)
    ]


dcterms.description[Funding] = """
Funding specifies information about funding received by an organization.

• receivedFrom: links to organization providing the funds. E.g., Ministry of Immigration, Refugees and Citizenship Canada (IRCC).
• fundersProgram: Specified if the funder has a program through which the funding is provided. E.g., Service Delivery Improvement.
• time:hasTime: Specifies a time interval over which the funding is awarded.
• requestedAmount: Amount requested by recipient organization.
• receivedAmount: Amount awarded by the funding organization.
• forStakeholder: Specifies the beneficary stakeholders for whom the funds are to be used for. E.g., Indigenous female youth.
• forProgram: Identifies the recipent organizations programs that the funding is to be used for.
"""