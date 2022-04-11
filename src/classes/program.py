from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms, ic
from src.utils import get_class


class Program(cids.Program):
    label = 'Program'
    is_a = [
        ic.hasAddress.only(ic.Address)
    ]


dcterms.description[Program] = """
The Program class extends cids:Program with an address field. This allows an organization to provide services at different locations.
For example, a “health” service can set up multiple offices closer to its clients.

• hasAddress: Address for the program.
"""