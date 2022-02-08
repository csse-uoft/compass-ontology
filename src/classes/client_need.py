from owlready2 import *
from src.namespaces import compass, cids, schema_old, dcterms
from src.utils import get_class


class NeedSatisfier(Thing):
    label = 'Need Satisfier'
    is_a = [
        compass.forNeed.only(get_class('ClientNeed')),
        compass.changes.only(get_class('Feature')),
        compass.hasSatisfierType.only(str),
        compass.hasImpact.only(str),
    ]


dcterms.description[NeedSatisfier] = """
A need satisfier is a way of meeting client needs. In our framework, need satisfiers are provided via social services. This helps define a clear, logical relationship, between the nature of a social service, i.e., the “need satisfier’ it provides, and the target need. For example, the particular qualities of counselling (a need satisfier) allow a social worker to believe, and reasonably expect, that referring a client who suffers from acute depression and wishes to move to a state of normal functioning to a provider of counselling (e.g., a registered therapist) would assist the client with meeting their need to improve their mental health state. 

We divide need satisfiers in the following categories:
•	resources (e.g., goods, money, facilities, housing)
•	knowledge and information (e.g., training, coaching, education, legal advice)
•	supports (e.g., companionship, supported transportation)

NeedSatisfier provides the following properties:
•	forNeed links to instances of Need that specify the client needs the satisfier (partially) fulfills
•	changes links to instances of ClientState that specify the client states changed by the satisfier
•	hasType identifes the type of satisfier, i.e., “Violator”, “Pseudo”, “Inhibiting”, “Singular”, “Synergistic”
•	hasImpact: specifies the level of belief that the good or service will satisfy the need
"""


class ClientFeature(Thing):
    label = 'Client Feature'
    is_a = [
        compass.affectsClientState.only(get_class('ClientState'))
    ]


class ClientNeed(Thing):
    label = 'Client Need'
    is_a = [
        compass.ofClient.only(get_class('Client')),
        compass.hasNeedSatisfier.only(NeedSatisfier),
        compass.hasImportance.only(str),
        compass.hasAcuityScore.only(str),
        compass.isExpressed.only(bool),
        compass.isNormative.only(bool),
        compass.hasNeedType.only(str),
        compass.hasChangeType.only(str),
        compass.hasFeature.only(ClientFeature),
        cids.hasDescription.only(str),
    ]


dcterms.description[ClientNeed] = """
Client needs are met via need satisfiers, such as counseling, language training, information about the local school system, translation and interpretation, etc. Need satisfiers are discussed in depth in the following section. 

Often client goals and needs, and the response to those needs (i.e., the provision of need satisfiers) are conflated during client assessments. For example, a person experiencing depression might be recorded as needing counselling, which is a need satisfier, instead of needing to improve their mental health state.

Our framework can help alleviate this issue by offering support for representing client problems, goals, needs and need satisfiers explicitly and avoiding conducting needs assessments based on fixed commitments to particular forms of action, i.e., dispensing a particular set of need satisfiers, or the services that provide them (if the agency/community of practice does not differentiate between need satisfiers and the services that supply them).

•	hasNeedSatisfier: links a ClientNeed instance with one or more satisfiers that may satisfy the need
•	hasImportance: specifies how important satisfying the need is from the perception of the client / legal guardian / social worker, e.g., “Low”, “Medium”, “High”, 1, 2, 3, etc.
•	hasAcuityScore: specifies the acuity of the need is to be satisfied, as assessed by a social worker / clinician, e.g., “Low”, “Medium”, “High”, 1, 2, 3
•	hasNeedType: this is one or more types selected from a taxonomy of needs
•	hasChangeType: specifies the type of change effected on a client’s state
"""
