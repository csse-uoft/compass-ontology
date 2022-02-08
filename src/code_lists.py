from owlready2 import *
from namespaces import compass, cids

class CL_Gender(cids.Code): pass


class CL_Ethnicity(cids.Code): pass


class CL_CA_AboriginalGroup(cids.Code): pass


class CL_Religion(cids.Code): pass


class CL_EducationType(cids.Code): pass


class CL_BirthStatus(cids.Code): pass


class CL_DeathCause(cids.Code): pass


class CL_JusticeSystemEventType(cids.Code): pass


class CL_HomelessCause(cids.Code): pass


class CL_HomelessType(cids.Code): pass


class CL_MaritalStatus(cids.Code): pass


class CL_RiskEventType(cids.Code): pass


class CL_Role(cids.Code): pass


class CL_Sex(cids.Code): pass


class CL_ImmigrationType(cids.Code): pass


class CL_Languages(cids.Code): pass


class CL_ServiceStatus(cids.Code): pass


class CL_EducationStatus(cids.Code): pass

class CL_EmploymentStatus(cids.Code): pass

class CL_ImmigrationStatus(cids.Code): pass

class CL_Temporality(cids.Code): pass

class CL_MilitaryStatus(cids.Code): pass

class CL_MilitaryBranch(cids.Code): pass

class CL_RCMPStatus(cids.Code): pass

class CL_RCMPBranch(cids.Code): pass

class CL_BirthStatus(cids.Code): pass

class CL_DeathCause(cids.Code): pass

class CL_MaritalStatus(cids.Code): pass

class CL_HousingType(cids.Code): pass

class CL_HousingCause(cids.Code): pass

class CL_NameCause(cids.Code): pass

class CL_GenderCause(cids.Code): pass

for gender in ['agender', 'ally', 'asexual', 'bigender', 'bisexual', 'female', 'gay',
               'gender_queer', 'gender_variant', 'intersex', 'lesbian', 'male', 'pangender',
               'pansexual', 'queer', 'questioning', 'transgender', 'transsexual', 'two_spirit']:
    CL_Gender(gender)

sex_male = CL_Sex("male")
sex_female = CL_Sex("female")

for education_type in ['bachelorArts', 'bachelorScience', 'bachelorAppliedScience', 'masterArts',
                       'masterScience', 'masterAppliedScience', 'phd', 'md', 'secondaryDegree']:
    CL_EducationType(education_type)

for justice_system_event_type in ['arrest', 'charged', 'beginIncarceration', 'endIncarceration',
                                  'beginParole', 'endParole', 'beginSentence', 'endSentence']:
    CL_JusticeSystemEventType(justice_system_event_type)

for status in ['scheduled', 'inProgress', 'completed']:
    CL_ServiceStatus(status)

for status in ['complete', 'inProgress', 'incomplete']:
    CL_EducationStatus(status)

for status in ['complete', 'quit', 'fired', 'retired', 'layedOff',
               'unemployed', 'selfEmployed', 'underEmployed']:
    CL_EmploymentStatus(status)

for name in ['temporary', 'permanent']:
    CL_Temporality(name)

for branch in ['airForce', 'army', 'navy']:
    CL_MilitaryBranch(branch)



# TODO: Individuals for: HomelessCause, HomelessType, MaritalStatus, RiskEventType, Role
