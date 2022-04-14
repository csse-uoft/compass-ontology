from owlready2 import *
from src.namespaces import compass, cids, act_50871, time, iso21972, tove_organization, \
    schema_old, xsd, ic, schema, dcterms, w3_org
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
Event is the super class of all events defined for a client. Events are used to log significant events that take place.

• hasName: a unique name/identifier for the event
• hasDescription: descriptions of the event
• occursAt: time interval during which the event occurs
• hasLocation: placename where the event occurred
• previousEvent: link to previous related event, if any
• nextEvent: link to next related event, if any
"""


class ClientEvent(Event):
    label = 'Client Event'
    is_a = [compass.forClient.exactly(1, get_class('Client'))]


dcterms.description[ClientEvent] = """
ClientEvents are used to log significant events that are relevant to a Client. They capture many types of personal events, such as Marriage, illness, employment, homelessness, etc. ClientEvent is a subclass of Event and inherits all of its properties, and adds the forClient property.

• forClient: identifies the client who is the subject of the event
"""


class ServiceEvent(ClientEvent):
    label = 'Service Event'
    is_a = [
        compass.hasStatus.max(1, compass['CL-ServiceStatus']),
        compass.atOrganization.exactly(1, cids.Organization),
        compass.forReferral.only(get_class('Referral'))
    ]


dcterms.description[ClientEvent] = """
A ServiceEvent is an event that changes a client in some way. It has the following properties: 

• hasStatus: status of the service.
• atOrganization: the organization providing the service.
• forReferral: the referral that led to the service event, if any.
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

• hasStatus: the status of the education event, complete, inProgress or incomplete.
• atOrganization: identifies the education organization the event took place.
• hasCertification: identifies the type of certification the education event has.
• hasType: identifies the type of education, including BA, BSC, etc.
"""


class EmploymentEvent(ClientEvent):
    label = 'Employment Event'
    is_a = [
        compass.atOrganization.exactly(1, cids.Organization),
        w3_org.holds.max(1, w3_org.Post),
        compass.hasStatus.exactly(1, compass['CL-EmploymentStatus']),
        compass.hasIncome.exactly(1, xsd.decimal)
    ]


dcterms.description[ClientEvent] = """
An EmploymentEvent is used to describe a client employment experience, such as working at a company for several years, where each change in role results in a new event, or working part time for a week. 

• atOrganization: The organization where the client works, if any. 
• org:holds: The post in the organization they hold, if any.
• hasStatus: The status of employment defined by CLEmploymentStatus, e.g., {completed, quit, fired, retired, layedOff, unemployed, selfEmployed, underEmployed}
• hasIncome: The annual income from their employment, if any.
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

• atOrganization: The organization where the client works, if any. 
• hasStatus: The status of employment defined by CL-ImmigrationStatus.
• hasImmigrationType: The status of the type of immigration defined by CL-ImmigrationType.
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

MedicalEvent is a subclass of ClientEvent and adds the following properties:
• hasCondition: a string value describing any condition of the client
• hasConditionTemporality: defines whether the condition is temporary, permanent, etc.
• atOrganization: identifies the organization where the event took place, if any.
• hasAddress: the address where the event took place.
• hasStatusStr: specifies any type of status information
"""


class MilitaryEvent(EmploymentEvent):
    label = "Military Event"
    is_a = [
        # TODO: atOrganization value canadianArmedForces
        compass.atOrganization.exactly(1, cids.Organization),
        # TODO: org:holds max 1 MilitaryPost
        # w3_org.holds.max(1, ),
        compass.hasStatus.exactly(1, compass['CL-MilitaryStatus']),
        compass.branch.only(compass['CL-MilitaryBranch'])
    ]


dcterms.description[MilitaryEvent] = """
A MilitaryEvent is used to describe a client’s military experiences. A separate military event would be created for each military experience of note. For example, change in rank, assignment to a new role, postings, etc. 

• atOrganization: specialized to being canadianArmedForces.
• org:holds: specialized to being a military post. (TBU)
• hasStatus: specialized to being military status.
• branch: the branch of the military their post is in.
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

• hasStatus: identifies the status of the birth.
• hasSex: identifies whether the baby is male or female.
• hasParent: identifies the persons who are the birth parent.
• forPerson: information on the baby.
"""


class DeathEvent(MedicalEvent):
    label = 'Death Event'
    is_a = [
        compass.forPerson.exactly(1, cids.Person),
        compass.hasCause.only(compass['CL-DeathCause'])
    ]


dcterms.description[DeathEvent] = """
A DeathEvent captures the death of a person that is important to the Client, including the client.

• forPerson: person who died (may not be the client)
• hasCause: identifies the cause of death.
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

• atOrganization: identifies the organization, e.g., hospital, where the birth took place, if any.
• hasAddress: the address where the birth took place.
• forPerson: identifies the two persons being married, separated or divorced.
• hasStatus: identifies the type of event: married, separated, divorced, reunited, …
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

• providingOrganization: identifies the organization that provided the housing, e.g., shelter, if homeless; housing project if government housing, etc. 
• providingProgram: The program of the providing organization that provided the housing.
• referringProgram: The program that referred the client to the providingProgram.
• hasAddress: The address where the client resided by homeless took place.
• hasPreviousAddress: The address of housing before this one.
• hasHousingType: The type of housing, e.g., house, apartment, condominium, shelter, rough sleeper, etc.
• hasCause: Identifies the cause of change of housing.
• contractDate: Date a lease or other type of housing contract is signed.
"""


class NameEvent(ClientEvent):
    label = 'Name Event'
    is_a = [
        # schema.givenName.exactly(1, str),
        schema.additionalName.only(str),
        # schema.familyName.exactly(1, str),
        compass.hasCause.only(compass['CL-NameCause']),
        compass.hasCauseComment.only(str),
    ]


dcterms.description[NameEvent] = """
A NameEvent captures the change of a client’s name. It has the following properties:

• schema:givenName: new given (first) name.
• schema:additionalName: new additional (middle) names.
• schema:familyName: new family (last) name.
• hasCause: identifies the cause/reason for the name change.
• hasCauseComment: additional information on the reason for the name change.
"""


class GenderEvent(ClientEvent):
    label = 'Gender Event'
    is_a = [
        compass.hasCause.only(compass['CL-GenderCause']),
    ]


dcterms.description[GenderEvent] = """
A GenderEvent captures the a change in the client’s gender. It has the following additional property:

• hasCause: identifies the cause of gender change.
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

• atOrganization: The organization where the justice system event took place, e.g., a court house, police station, etc.
• hasStatus: the status of the event, for now is simply a string.
• eventType: is the type of justice event constrained to being and instance of the code list CL-JusticeSystemEventType.
"""


class RiskEvent(ClientEvent):
    label = 'Risk Event'
    is_a = [
        compass.hasStatusStr.exactly(1, str),
        compass.eventType.only(compass['CL-RiskEventType']),
        compass.causedBy.only(Event)
    ]


dcterms.description[RiskEvent] = """
A RiskEvent captures the occurrence of a client being at risk.

As a subclass of ClientEvent it captures the client, time interval and location, plus the following additional properties:
• hasStatus: the status of the event, for now is simply a string.
• eventType: is the type of risk event constrained to being and instance of the code list CL-RiskEventType.
• causedBy: Identifies zero or more events that may have caused this risk, for example a loss of employment even may lead to a risk of homelessness.
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
Client interactions with service providers through a computer application requires logging capabilities to capture related information.

• hasUserStakeholder: the stakeholder that was using the application when the event was created
• dateCreated: timestamp when the event was created
• hasSource: the URL or unique address where this event originated
• hasMetaData: the information stored with the event
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
ServiceFailureEvent represents an event triggered when there is a barrier that prevents clients from using a service they are otherwise eligible for. 

• forService: the Service or Activity this failure event indicates cannot be used by a client
• hasCharacteristic: the characteristic that caused the failure.
• hasFailureType: the Service or Activity type that is preventing the stakeholder from using the service (e.g. Transportation, etc)
• hasDescription: description of the failure type
"""
