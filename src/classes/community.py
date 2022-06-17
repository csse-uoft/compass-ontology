from owlready2 import Thing
from src.namespaces import compass, cids, schema, tove_organization, xsd, city_50872, dcterms
from src.utils import get_class


class CommunityCharacteristic(Thing):
    label = 'Community Characteristic'
    is_a = [
        cids.hasCharacteristic.only(cids.Characteristic),
        compass.hasNumber.exactly(1, xsd.NonNegativeInteger)
    ]


dcterms.description[CommunityCharacteristic] = """
The CommunityCharacteristic references the identifying characteristics that several individauls have in common that in turn makes them a community.
•	hasCommunityCharacteristic: the characteristic that defines this Community
•	hasNumber: the number of people in the community (not all individuals in a spatial area (neighborhood), only those that fit the CommunityCharacteristic profile
"""


class Community(city_50872.CityAdministrativeArea):
    label = 'Community'
    is_a = [
        compass.hasCommunityCharacteristic.only(CommunityCharacteristic)
    ]


dcterms.description[Community] = """
A community is made up 2 or more individuals that share some properties. These properties are represented as characteristics of the community. Hence, a Community class has the following property:
•	hasCommunityCharacteristic: characteristics of the community this class represents
"""
