from owlready2 import *
from ..namespaces import compass, cids, tove_organization, time, iso21972, ic
from ..utils import get_class


class hasName(DataProperty):
    range = [str]
    # python_name = 'has_name'


class hasGender(ObjectProperty):
    namespace = compass
    domain = []
    range = [get_class('CL-Gender')]


class hasSex(ObjectProperty):
    range = [get_class('CL-Sex')]


class hasEthnicity(ObjectProperty):
    range = [get_class('CL-Ethnicity')]
    # python_name = 'has_ethnicity'


class membeOfAboriginalGroup(ObjectProperty):
    range = [get_class('CL-CA-AboriginalGroup')]


class hasReligion(ObjectProperty):
    range = [get_class('CL-Religion')]


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


class hasState(ObjectProperty):
    pass


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
    range = [get_class('CL-EducationType')]


class hasImmigrationType(ObjectProperty):
    range = [get_class('CL-ImmigrationType')]


class hasProficiency(ObjectProperty): pass


class birthLanguage(DataProperty): pass


class homeLanguage(DataProperty): pass


class hasAddress(ObjectProperty):
    equivalent_to = [ic.hasAddress]


class hasFocus(ObjectProperty):
    pass


class hasMode(ObjectProperty):
    pass


class hasRequirement(ObjectProperty):
    pass


class providesService(ObjectProperty):
    pass


class mappedTo(ObjectProperty):
    pass


class hasOrganization(ObjectProperty):
    pass


class hasIncome(DataProperty):
    pass


class hasLanguage(ObjectProperty):
    pass


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
