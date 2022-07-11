from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms, ic
from src.utils import get_class


class Organization(cids.Organization):
    label = 'Organization'
    is_a = [
        compass.hasFunding.only(get_class('Funding')),
        compass.hasLanguage.only(get_class('CL-Language')),
        ic.hasEmail.only(str),
    ]


dcterms.description[Organization] = """
The Compass Organization extends cids:Organization with funding information.

• hasFunding: links to instances of Funding that specify the funding received by the organization.
• hasLanguage: Language for the Organization.
• hasEmail: Email for the Organization.
"""