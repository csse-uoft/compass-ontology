from owlready2 import *
from src.namespaces import compass, cids, tove_organization, time, iso21972, ic
from src.code_lists import CL_Gender, CL_Ethnicity, CL_CA_AboriginalGroup, CL_Religion, \
    CL_EducationType, \
    CL_ImmigrationType
from src.utils import get_class


class hasName(DataProperty):
    range = [str]
    # python_name = 'has_name'


class hasGender(ObjectProperty):
    namespace = compass
    domain = []
    range = [get_class('Gender')]  # Or [compass.CL_Gender]
    python_name = 'has_gender'


class hasSex(ObjectProperty):
    range = [get_class('Sex')]


class hasEthnicity(ObjectProperty):
    range = [CL_Ethnicity]
    # python_name = 'has_ethnicity'


class membeOfAboriginalGroup(ObjectProperty):
    range = [CL_CA_AboriginalGroup]


class hasReligion(ObjectProperty):
    range = [CL_Religion]


class hasDependent(ObjectProperty):
    range = [cids.Person]


class hasOutcome(ObjectProperty):
    range = [cids.StakeholderOutcome]


class hasNeed(ObjectProperty):
    range = [get_class('ClientNeed')]  # Cannot use 'compass.Need' since Need is not defined

    pass


class hasGoal(ObjectProperty):
    range = [tove_organization.Goal]


class hasProblem(ObjectProperty):
    range = []


class hasStatus(ObjectProperty):
    pass


class hasClientState(ObjectProperty):
    range = [get_class('ClientState')]


class hasAcuityScore(DataProperty):
    range = [str]


# ------ Event related --------

class occursAt(DataProperty):
    range = [time.Interval]


class hasLocation(DataProperty):
    range = [iso21972.Feature]


class previousEvent(ObjectProperty):
    range = [get_class('Event')]


class nextEvent(ObjectProperty):
    range = [get_class('Event')]


class forClient(ObjectProperty):
    range = [get_class('Event')]


class hasEducationEvent(ObjectProperty):
    range = [get_class('Event')]


class hasEmploymentEvent(ObjectProperty):
    range = [get_class('Event')]


class hasImmigrationEvent(ObjectProperty):
    range = [get_class('Event')]


class hasMedicalEvent(ObjectProperty):
    range = [get_class('Event')]


class hasHousingEvent(ObjectProperty):
    range = [get_class('Event')]


class hasNameEvent(ObjectProperty):
    range = [get_class('Event')]


class hasGenderEvent(ObjectProperty):
    range = [get_class('Event')]


class hasBirthEvent(ObjectProperty):
    range = [get_class('Event')]


class hasDeathEvent(ObjectProperty):
    range = [get_class('Event')]


class hasMaritalEvent(ObjectProperty):
    range = [get_class('Event')]


class hasHomelessEvent(ObjectProperty):
    range = [get_class('Event')]


class hasJusticeSystemEvent(ObjectProperty):
    range = [get_class('Event')]


class atOrganization(ObjectProperty): pass


class hasCertification(ObjectProperty): pass


class hasType(ObjectProperty):
    range = [CL_EducationType]


class hasImmigrationType(ObjectProperty):
    range = [CL_ImmigrationType]


class hasProficiency(DataProperty): pass


class birthLanguage(DataProperty): pass


class homeLanguage(DataProperty): pass


class hasAddress(ObjectProperty):
    equivalent_to = [ic.hasAddress]


data_properties = [
    'hasCondition', 'hasStatusStr', 'hasCauseComment'
]

object_properties = [
    'hasConditionTemporality', 'branch', 'hasParent', 'forPerson', 'hasCause', 'providingOrganization',
    'providingProgram', 'referringProgram', 'hasPreviousAddress', 'hasHousingType', 'contractDate', 'eventType',
    'causedBy'
]

for data_property in data_properties:
    type(data_property, (DataProperty,), {})

for object_property in object_properties:
    type(object_property, (ObjectProperty,), {})
