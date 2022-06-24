from owlready2 import *
from src.namespaces import compass, cids

code_lists_str = [
    'CL-Gender', 'CL-Ethnicity', 'CL-CA-AboriginalGroup', 'CL-Religion', 'CL-EducationType', 'CL-BirthStatus',
    'CL-DeathCause', 'CL-JusticeSystemEventType', 'CL-HomelessCause', 'CL-HomelessType', 'CL-MaritalStatus',
    'CL-RiskEventType', 'CL-Role', 'CL-Sex', 'CL-ImmigrationType', 'CL-Languages', 'CL-ServiceStatus',
    'CL-EducationStatus', 'CL-EmploymentStatus', 'CL-ImmigrationStatus', 'CL-Temporality', 'CL-MilitaryStatus',
    'CL-MilitaryBranch', 'CL-RCMPStatus', 'CL-RCMPBranch', 'CL-HousingType', 'CL-HousingCause', 'CL-NameCause',
    'CL-GenderCause', 'CL-CatchmentArea', 'CL-ServiceMode', 'CL-LanguageProficiency'
]

for code in code_lists_str:
    type(code, (cids.Code,), {})

for gender in ['agender', 'ally', 'asexual', 'bigender', 'bisexual', 'female', 'gay',
               'gender_queer', 'gender_variant', 'intersex', 'lesbian', 'male', 'pangender',
               'pansexual', 'queer', 'questioning', 'transgender', 'transsexual', 'two_spirit']:
    compass['CL-Gender'](gender)

sex_male = compass['CL-Sex']("male")
sex_female = compass['CL-Sex']("female")

for education_type in ['bachelorArts', 'bachelorScience', 'bachelorAppliedScience', 'masterArts',
                       'masterScience', 'masterAppliedScience', 'phd', 'md', 'secondaryDegree']:
    compass['CL-EducationType'](education_type)

for justice_system_event_type in ['arrest', 'charged', 'beginIncarceration', 'endIncarceration',
                                  'beginParole', 'endParole', 'beginSentence', 'endSentence']:
    compass['CL-JusticeSystemEventType'](justice_system_event_type)

for status in ['scheduled', 'inProgress', 'completed']:
    compass['CL-ServiceStatus'](status)

for status in ['complete', 'inProgress', 'incomplete']:
    compass['CL-EducationStatus'](status)

for status in ['complete', 'quit', 'fired', 'retired', 'layedOff',
               'unemployed', 'selfEmployed', 'underEmployed']:
    compass['CL-EmploymentStatus'](status)

for name in ['temporary', 'permanent']:
    compass['CL-Temporality'](name)

for branch in ['airForce', 'army', 'navy']:
    compass['CL-MilitaryBranch'](branch)

for mode in ['in-person', 'phone', 'online', 'offline']:
    compass['CL-ServiceMode'](mode)

for language_proficiency in ['native', 'fluent']:
    compass['CL-LanguageProficiency'](language_proficiency)

for language in ['english', 'french']:
    compass['CL-Languages'](language)

# TODO: Individuals for: HomelessCause, HomelessType, MaritalStatus, RiskEventType, Role
