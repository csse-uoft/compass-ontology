from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms, ic
from src.utils import get_class


class HelpSeekerCode(cids.Code):
    label = 'HelpSeeker Code'


helpseeker = compass.Organization('HelpSeeker')
compass.hasOrganization[HelpSeekerCode] = [helpseeker]
dcterms.description[HelpSeekerCode] = """
The cids:Code is defined by an organization that is identified by the hasOrganization property.
The HelpSeekerCode class is custom for Help Seeker codes. Any code defined as a HelpSeekerCode instance is defined by HelpSeeker Technologies.

• hasOrganization: Points to the Help Seeker Technologies company.
"""