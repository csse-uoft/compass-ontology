from owlready2 import *
from src.namespaces import compass, cids, schema, tove_organization, dcterms
from src.utils import get_class


class Client(cids.Person):
    label = 'Client'
    from .language_ability import LanguageAbility
    from .client_need import ClientNeed
    from .client_problem import ClientProblem
    from .client_status import ClientStatus
    from .client_state import ClientState

    is_a = [
        compass.satisfiesStakeholder.only(cids.Stakeholder),
        compass.hasGender.max(1, compass['CL-Gender']),
        # compass.hasSex.max(1, compass.Sex),
        compass.hasEthnicity.only(compass['CL-Ethnicity']),
        compass.membeOfAboriginalGroup.only(compass['CL-CA-AboriginalGroup']),
        compass.hasReligion.only(compass['CL-Religion']),
        compass.hasDependent.only(cids.Person),
        schema.knowsLanguage.only(LanguageAbility),

        compass.hasServiceEvent.only(get_class('ServiceEvent')),
        compass.hasEducationEvent.only(get_class('EducationEvent')),
        compass.hasEmploymentEvent.only(get_class('EmploymentEvent')),
        compass.hasImmigrationEvent.only(get_class('ImmigrationEvent')),
        compass.hasMedicalEvent.only(get_class('MedicalEvent')),
        compass.hasMaritalEvent.only(get_class('MaritalEvent')),

        compass.hasHousingEvent.only(get_class('HousingEvent')),
        compass.hasNameEvent.only(get_class('NameEvent')),
        compass.hasGenderEvent.only(get_class('GenderEvent')),
        compass.hasBirthEvent.only(get_class('BirthEvent')),
        compass.hasDeathEvent.only(get_class('DeathEvent')),
        compass.hasJusticeSystemEvent.only(get_class('JusticeSystemEvent')),

        compass.hasOutcome.only(cids.StakeholderOutcome),
        compass.hasNeed.only(ClientNeed),
        compass.hasGoal.only(tove_organization.Goal),
        compass.hasProblem.only(ClientProblem),
        compass.hasStatus.only(ClientStatus),
        compass.hasState.only(ClientState),
        compass.hasAcuityScore.exactly(1, str),
    ]


dcterms.description[Client] = """
Client inherits all properties of 5087-2:Person and cids:Stakeholder. The following graph depicts the main classes and properties in the cids:Stakeholder.  Please refer to the CIDS manual for further details.

Client extends these classes with the following properties:
•	satisfiesStakeholder: Identifies the stakeholder specifications that the client satisfies.
•	hasGender: A coded property specifying the gender.
•	hasEthnicity: A coded property specifying known ethnicities of the client.
•	memberOfAboriginalGroup: A coded property identifying the aboriginal group the client is a member of, if any.
•	hasReligion: A coded property specifying known religions of the client.
•	hasDependent: A set of Person instances.
•	schema:knowsLanguage: links to instances of LanguageAbility that specifies languages known and proficiency.

•	hasServiceEvent: links to instances of ServiceEvent, each defining a service the client has received.
•	hasEducationEvent: links to instances of EducationEvent, each defining education the client has received.
•	hasEmploymentEvent: links to instances of EmploymentEvent.
•	hasImmigrationEvent: links to instances of ImmigrationEvent, each defining stages of immigration, if relevant.
•	hasMedicalEvent: links to instances of MedicalEvent, each defining separate medical conditions, including births and deaths, which are subclasses.
•	hasMaritalEvent: links to instances of MaritalEvent

•	hasHousingEvent: links to instances of HousingEvent that tracks changes in housing including homelessness.
•	hasNameEvent: links to instances of NameEvent.
•	hasGenderEvent: links to instances of GenderEvent.
•	hasBirthEvent: links to instances of BirthEvent associated with the client.
•	hasDeathEvent: links to instances of DeathEvent associated with the client.
•	hasHomelessEvent: links to instances of HomelessEvent associated with the client.
•	hasJusticeSystemEvent: links to instances of JusticeSystemEvent.

•	hasOutcome links to instances of StakeholderOutcome that specify the outcomes experienced by the client.
•	hasNeed: links to instances of Need that specify the needs of the client.
•	hasGoal: links to instances of Goal that specify the goals of the client.
•	hasProblem: links to instances of Problem that specify the problems of the client.
•	hasStatus: links to instances of Status that specify the status of the client.
•	hasClientState: links to instances of ClientState that specify the state the client is in.
•	hasAcuityScore specifies the acuity of the need is to be satisfied, as assessed by a social worker / clinician, e.g., “Low”, “Medium”, “High”, 1, 2, 3.
"""
