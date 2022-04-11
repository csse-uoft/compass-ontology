from owlready2 import *
from src.namespaces import compass, cids, act_50871, time, iso21972, tove_organization, \
    schema_old, xsd, ic, schema, dcterms
from src.utils import get_class


class Event(act_50871.State):
    label = 'Event'
    is_a = [compass.hasName.exactly(1, str),
            cids.hasDescription.only(str),
            compass.occursAt.exactly(1, time.Interval),
            compass.hasLocation.exactly(1, iso21972.Feature)]


# This references itself, need define it separately
Event.is_a.append(compass.previousEvent.exactly(1, Event))
Event.is_a.append(compass.nextEvent.exactly(1, Event))

dcterms.description[Event] = """
An Event describes something that occurs at some location, at some time, and involving a Client. It can describe the client as being the subject of an action, or a change of state. A taxonomy of events follows its definition.

The basic Event class as the following properties:
•	hasName: a unique name/identifier for the event
•	hasDescription: descriptions of the event
•	occursAt: time interval during which the event occurs
•	hasLocation: placename where the event occurred
•	previousEvent: link to previous related event, if any
•	nextEvent: link to next related event, if any
"""


class ClientEvent(Event):
    label = 'Client Event'
    is_a = [compass.forClient.exactly(1, get_class('Client'))]


dcterms.description[ClientEvent] = """
ClientEvents are used to log significant events that are relevant to a Client. They capture many types of personal events, such as Marriage, illness, employment, homelessness, etc. ClientEvent is a subclass of Event and inherits all of its properties, and adds the forClient property.
"""


class ServiceEvent(ClientEvent):
    label = 'Service Event'
    is_a = [
        compass.hasStatus.max(1, compass['CL-ServiceStatus']),
        compass.atOrganization.exactly(1, cids.Organization),
        compass.forReferral.only(get_class('Referral'))
    ]


dcterms.description[ClientEvent] = """
Compass has the capability of accessing services that have been assigned to or used by a client. It also has the capability to ask outcome related questions related to the services clients receive.  To support this the ServiceEvent is used to represent actual services that have been scheduled for, in progress or completed for a Client.

An ServiceEvent is a subclass of ClientEvent and adds the following properties:
•	hasStatus: status of the service.
•	atOrganization: the organization providing the service.
•	forReferral: the referral that led to the service event, if any.
"""


class Certification(Thing):
    pass


class EducationEvent(ClientEvent):
    label = 'Education Event'
    is_a = [
        compass.hasStatus.exactly(1, compass['CL-EducationStatus']),
        compass.atOrganization.exactly(1, cids.Organization),
        compass.hasCertification.some(Certification),
        compass.hasType.only(compass['CL-EducationType'])
    ]


dcterms.description[EducationEvent] = """
An EducationEvent is used to describe a client educational or training experience, such as having a BSc, or taken first aid training.
•	Competency Questions
•	What is the maximum education level completed by the client?
•	What is the current education enrolment status of the client ?
•	Example service eligibility criteria:
•	18+ Low income Metis full time student
•	Immigrant women, including Canadian citizens and refugees with less than 7 years of education
•	University of Calgary staff and students
•	University of Lethbridge students
•	Women pursuing post-secondary education

An EducationEvent is a subclass of ClientEvent and adds the following properties:
•	hasStatus: the status of the education event, complete, inProgress or incomplete.
•	atOrganization: identifies the education organization the event took place.
•	hasCertification: identifies the type of certification the education event has.
•	hasType: identifies the type of education, including BA, BSC, etc.
"""


class EmploymentEvent(ClientEvent):
    label = 'Employment Event'
    is_a = [
        compass.atOrganization.exactly(1, cids.Organization),
        # TODO: tove_organization.holds.max(1, tove_organization.Post),
        compass.hasStatus.exactly(1, compass['CL-EmploymentStatus'])
    ]


dcterms.description[ClientEvent] = """
An EmploymentEvent is used to describe a client employment experience, such as working at a company for several years, where each change in role results in a new event, or working part time for a week.
•	Competency Questions
•	Is the client currently employed? 
•	Is the client currently earning an income?
•	When did the client start their current employment?
•	When did the client stopped working?
•	What is the employment status of the client (e.g., employed full/part-time, unemployed, underemployed, self-employed, looking for work)?
•	Example service eligibility criteria:
•	Albertans earning an income
•	First Nation members who are unemployed
•	Indigenous people under or unemployed, interested in pursuing a trade
•	Single parent adults 18+ residing in Red Deer and area who are unemployed or marginally employed
•	Unemployed or under-employed Albertans
•	Unemployed permanent residents, citizens or persons legally entitled to work in Canada
•	Unemployed youth (17-30 years of age) able to attend training and looking for employment

EmploymentEvent is a subclass of ClientEvent and adds the following properties:
•	atOrganization: The organization where the client works, if any. 
•	org:holds: The post in the organization they hold, if any.
•	hasStatus: The status of employment defined by CLEmploymentStatus, e.g., {completed, quit, fired, retired, layedOff, unemployed, selfEmployed, underEmployed}
•	hasIncome: The annual income from their employment, if any.
"""


class ImmigrationEvent(ClientEvent):
    label = 'Immigration Event'
    is_a = [
        compass.atOrganization.exactly(1, cids.Organization),
        compass.hasStatus.exactly(1, compass['CL-ImmigrationStatus']),
        compass.hasImmigrationType.exactly(1, compass['CL-ImmigrationType'])
    ]


dcterms.description[ImmigrationEvent] = """
An ImmigrationEvent is used to describe a client immigration record. A separate immigration event would be created for each step in the immigration process.

EmploymentEvent is a subclass of ClientEvent and adds the following properties:
•	atOrganization: The organization where the client works, if any. 
•	hasStatus: The status of employment defined by CL-ImmigrationStatus.
•	hasImmigrationType: The status of the type of immigration defined by CL-ImmigrationType.
"""


class MedicalEvent(ClientEvent):
    label = 'Medical Event'
    is_a = [
        compass.hasCondition.only(str),
        compass.hasConditionTemporality.only(compass['CL-Temporality']),
        compass.atOrganization.exactly(1, cids.Organization),
        compass.hasStatusStr.exactly(1, str)
    ]


dcterms.description[MedicalEvent] = """
A MedicalEvent is used to describe client medical events. A separate medical event would be created for each medical problem, test, visit, etc.

•	Competency Questions
•	What medical condition does the client have? (e.g., chronic disability, chronic/acute illness, injury, risky/ pregnancy, postpartum)
•	What type of disability does the client have?
•	What type of chronic illness does the client suffer from?
•	Example service eligibility criteria:
•	16+  who have been diagnosed with FASD
•	16+ with a disability
•	17 years or younger with an acute psychiatric illness
•	Whitecourt residents who need support due to disability, illness, frailty or injury
•	Visually compromised
•	Women after delivery
•	Women carrying more than one baby
•	Women during pregnancy and up to one year after they give birth
•	Women greater than 20 weeks gestation

MedicalEvent is a subclass of ClientEvent and adds the following properties:
•	hasCondition: a string value describing any condition of the client
•	hasConditionTemporality: defines whether the condition is temporary, permanent, etc.
•	atOrganization: identifies the organization where the event took place, if any.
•	hasAddress: the address where the event took place.
•	hasStatusStr: specifies any type of status information
"""


class MilitaryEvent(EmploymentEvent):
    label = "Military Event"
    is_a = [
        compass.atOrganization.exactly(1, cids.Organization),
        # TODO: org:holds max 1 MilitaryPost
        compass.hasStatus.exactly(1, compass['CL-MilitaryStatus']),
        compass.branch.only(compass['CL-MilitaryBranch'])
    ]


dcterms.description[MilitaryEvent] = """
A MilitaryEvent is used to describe a client’s military experiences. A separate military event would be created for each military experience of note. For example, change in rank, assignment to a new role, postings, etc.

•	Competency Questions
•	Is the client a veteran?
•	Define what is a veteran, e.g., former member of the Canadian Armed Forces who successfully underwent basic training and was honourably discharged after two years active duty. 
•	Is the client an active member of the military?
•	Example service eligibility criteria:
•	Veterans who are homeless
•	Veterans, current military members

MilitaryEvent is a subclass of EmploymentEvent and adds the following properties:
•	atOrganization: specialized to being canadianArmedForces.
•	org:holds: specialized to being a military post. (TBU)
•	hasStatus: specialized to being military status.
•	branch: the branch of the military their post is in.
"""


class RCMPEvent(EmploymentEvent):
    label = 'RCMP Event'
    is_a = [
        compass.atOrganization.exactly(1, cids.Organization),
        # TODO: org:holds max 1 RCMPPost
        compass.hasStatus.exactly(1, compass['CL-RCMPStatus']),
        compass.branch.only(compass['CL-RCMPBranch'])
    ]


dcterms.description[RCMPEvent] = """
A RCMPEvent is used to describe a client’s RCMP experiences. A separate RCMP event would be created for each RCMP experience of note. For example, change in rank, assignment to a new role, postings, etc.

•	Competency Questions
•	Is the client an active member of the RCMP?
•	Example service eligibility criteria:
•	Current RCMP members

RCMPEvent is a subclass of EmploymentEvent and adds the following properties:
•	atOrganization: specialized to being rcmp.
•	org:holds: specialized to being a RCMP post. (TBU)
•	hasStatus: specialized to being RCMP status.
•	branch: the branch of the RCMP their post is in.
"""


class BirthEvent(MedicalEvent):
    label = 'Birth Event'
    is_a = [
        compass.hasStatus.exactly(1, compass['CL-BirthStatus']),
        compass.hasSex.exactly(1, compass['CL-Sex']),
        compass.hasParent.max(2, cids.Person),
        compass.forPerson.exactly(1, cids.Person)
    ]


dcterms.description[BirthEvent] = """
A BirthEvent captures a birth that is important to the Client, including the client.

A BirthEvent is a subclass of MedicalEvent and adds the following properties:
hasStatus: identifies the status of the birth.
•	hasSex: identifies whether the baby is male or female.
•	hasParent: identifies the persons who are the birth parent.
•	forPerson: information on the baby.
"""


class DeathEvent(MedicalEvent):
    label = 'Death Event'
    is_a = [
        compass.forPerson.exactly(1, cids.Person),
        compass.hasCause.only(compass['CL-DeathCause'])
    ]


dcterms.description[DeathEvent] = """
A DeathEvent captures the death of a person that is important to the Client, including the client.

A DeathEvent is a subclass of MedicalEvent and adds the following properties:
•	forPerson: person who died (may not be the client)
•	hasCause: identifies the cause of death.
"""


class MaritalEvent(ClientEvent):
    label = 'Marital Event'
    is_a = [
        compass.atOrganization.max(1, cids.Organization),
        ic.hasAddress.exactly(1, ic.Address),
        compass.forPerson.exactly(1, cids.Person),
        compass.hasStatus.exactly(1, compass['CL-MaritalStatus']),
    ]


dcterms.description[MaritalEvent] = """
A MaritalEvent captures the marriage, divorce, separation, etc. of importance to the client.

A MaritalEvent is a subclass of ClientEvent and adds the following properties:
•	atOrganization: identifies the organization, e.g., hospital, where the birth took place, if any.
•	hasAddress: the address where the birth took place.
•	forPerson: identifies the two persons being married, separated or divorced.
•	hasStatus: identifies the type of event: married, separated, divorced, reunited, …
"""


class HousingEvent(ClientEvent):
    label = 'Housing Event'
    is_a = [
        compass.providingOrganization.max(1, cids.Organization),
        compass.providingProgram.max(1, cids.Program),
        compass.referringProgram.max(1, cids.Program),
        ic.hasAddress.exactly(1, ic.Address),
        compass.hasPreviousAddress.exactly(1, ic.Address),
        compass.hasHousingType.exactly(1, compass['CL-HousingType']),
        compass.hasCause.only(compass['CL-HousingCause']),
        compass.contractDate.max(1, time.Instant)
    ]


dcterms.description[HousingEvent] = """
A HousingEvent captures a single contiguous span of housing experienced by the client. It covers both regular housing and homelessness.

•	providingOrganization: identifies the organization that provided the housing, e.g., shelter, if homeless; housing project if government housing, etc. 
•	providingProgram: The program of the providing organization that provided the housing.
•	referringProgram: The program that referred the client to the providingProgram.
•	hasAddress: The address where the client resided by homeless took place.
•	hasPrviousAddress: The address of housing before this one.
•	hasHousingType: The type of housing, e.g., house, apartment, condominium, shelter, rough sleeper, etc.
•	hasCause: Identifies the cause of change of housing.
•	contractDate: Date a lease or other type of housing contract is signed.
"""


class NameEvent(ClientEvent):
    label = 'Name Event'
    is_a = [
        schema.givenName.exactly(1, str),
        schema.additionalName.only(str),
        schema.familyName.exactly(1, str),
        compass.hasCause.only(compass['CL-NameCause']),
        compass.hasCauseComment.only(str),
    ]


dcterms.description[NameEvent] = """
A NameEvent captures the change of a client’s name. It has the following properties:

•	schema:givenName: new given (first) name.
•	schema:additionalName: new additional (middle) names.
•	schema:familyName: new family (last) name.
•	hasCause: identifies the cause/reason for the name change.
•	hasCauseComment: additional information on the reason for the name change.
"""


class GenderEvent(ClientEvent):
    label = 'Gender Event'
    is_a = [
        compass.hasCause.only(compass['CL-GenderCause']),
    ]


dcterms.description[GenderEvent] = """
A GenderEvent captures the a change in the client’s gender. It has the following additional property:
•	hasCause: identifies the cause of gender change.
"""


class JusticeSystemEvent(ClientEvent):
    label = 'Justice System Event'
    is_a = [
        compass.atOrganization.max(1, cids.Organization),
        compass.hasStatusStr.exactly(1, str),
        compass.eventType.only(compass['CL-JusticeSystemEventType'])
    ]


dcterms.description[JusticeSystemEvent] = """
A JusticeSystemEvent is used to describe a client’s experiences with the justice system. A separate event would be created for each justice system experience of note. For example, arrests, incarcerations, releases, etc.

•	Competency System History
•	Was the client a victim of a crime?
•	What type of crime was the client a victim of?
•	Was the client convicted of a crime?
•	Define victim, e.g., a person who has suffered physical or emotional harm, property damage, or economic loss as a result of a crime
•	Example service eligibility criteria:
•	Victims and survivors affected by impaired driving.
•	Victims and witnesses of a crime or tragedy
•	Victims of sexual assault (14 years & older)
•	Women parolees
•	Women who are incarcerated

A JusticeSystemEvent is a subclass of ClientEvent and as the following additional properties:
•	atOrganization: The organization where the justice system event took place, e.g., a court house, police station, etc.
•	hasStatus: the status of the event, for now is simply a string.
•	eventType: is the type of justice event constrained to being and instance of the code list CL-JusticeSystemEventType.
"""


class RiskEvent(ClientEvent):
    label = 'Risk Event'
    is_a = [
        compass.hasStatusStr.exactly(1, str),
        compass.eventType.only(compass['CL-RiskEventType']),
        compass.causedBy.only(Event)
    ]


dcterms.description[RiskEvent] = """
A RiskEvent captures the occurrence of a client being at risk.  It addresses the following competency questions and requirements: 
•	Risk status
•	What vulnerability is the client at risk of?
•	Relevant service eligibility criteria:
•	Women at risk of or experiencing domestic violence.
•	Women experiencing or at risk of homelessness
•	Women who are at risk for delivering low birth-weight babies
•	Women who are at risk of giving birth to a baby that has been exposed to alcohol during pregnancy
•	Vulnerable youth in the Foothills region between the ages of 14-24

As a subclass of ClientEvent it captures the client, time interval and location, plus the following additional properties:
•	hasStatus: the status of the event, for now is simply a string.
•	eventType: is the type of risk event constrained to being and instance of the code list CL-RiskEventType.
•	causedBy: Identifies zero or more events that may have caused this risk, for example a loss of employment even may lead to a risk of homelessness.
"""


class StakeholderEvent(Event):
    label = 'Stakeholder Event'
    is_a = [
        cids.forStakeholder.exactly(1, cids.Stakeholder)
    ]


dcterms.description[StakeholderEvent] = """
The cids:Stakeholder class is a subclass of an Organization or Person and identifies a person or organization required to answer the above competency questions. 
The use cases include competency questions such as: 
•	How many users interacted with service?
•	How long did #6 stay in counselling?
•	How are people looking for help?

The StakeholderEvent captures events performed by stakeholders.

•	forStakeholder: the stakeholder that created this Event instance.
"""


class AppEvent(Event):
    label = 'Application Event'
    is_a = [
        compass.hasApplication.exactly(1, get_class('Application')),
        compass.hasUserStakeholder.exactly(1, get_class('Stakeholder')),
        schema_old.dateCreated.exactly(1, xsd.dataTime),
        compass.hasSource.only(str),
        compass.hasMetaData.only(str),
    ]


dcterms.description[AppEvent] = """
Client interactions with service providers through a computer application requires logging capabilities to answer capture related use cases. The use cases include competency questions such as: 
•	Who are the highest systems users currently?
•	How many are there that meet benchmarks for high users?
•	What are the system interactions patterns for these clients over past 3 mo ? What about past month?

•	An AppEvent is a subclass of Event. It defines an event that was created by an Application instance, and captures any information relevant to that event, such as the application itself, user information, a timestamp, the URL the event came from, and any information embedded in the event, such as messages being sent by the applica as Applicationcation: the application this event was created in
•	hasUserStakeholder: the stakeholder that was using the application when the event was created
•	dateCreated: timestamp when the event was created
•	hasSource: the URL or unique address where this event originated
•	hasMetaData: the information stored with the event
"""


class ServiceFailureEvent(Event):
    label = 'Service Failure Event'
    is_a = [
        compass.forService.only(cids.Service | cids.Activity),
        cids.hasCharacteristic.only(cids.Characteristic),
        compass.hasFailureType.only(cids.Service | cids.Activity | get_class('ServiceBarrier')),
        cids.hasDescription.only(str)
    ]


dcterms.description[ServiceFailureEvent] = """
ServiceFailureEvent represents an event triggered when there is a barrier that prevent clients from using a service they are otherwise eligible for. This class captures service events that cover the following competency questions.

•	Which of these services am I or my family eligible for?
•	What are the barriers to service experience by the client?
•	Is there a cost for x service?

The ServiceFailureEvent class has the following properties:

•	forService: the Service or Activity this failure event indicates cannot be used by a client
•	hasCharacteristic: the characteristic that caused the failure.
•	hasFailureType: the Service or Activity type that is preventing the stakeholder from using the service (e.g. Transportation, etc)
•	hasDescription: description of the failure type
"""
