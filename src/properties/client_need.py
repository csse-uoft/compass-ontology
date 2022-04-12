from owlready2 import DataProperty, ObjectProperty
from src.namespaces import compass, cids, tove_organization, time, iso21972
from src.utils import get_class


class isBarrierFor(ObjectProperty):
    range = [get_class('ClientState')]


class hasTimeScale(DataProperty):
    range = [str]


class hasTimeHorizon(DataProperty):
   pass


class hasStartDate(ObjectProperty):
    range = [time.DateTimeDescription]


class hasEndDate(ObjectProperty):
    range = [time.DateTimeDescription]


class inducesClientState(ObjectProperty):
    range = [get_class('ClientState')]


class inducesState(ObjectProperty):
    pass


class inducedByEvent(ObjectProperty):
    range = [get_class('Event')]


class hasDuration(ObjectProperty):
    range = [time.GeneralDurationDescription]


class inducesGoal(ObjectProperty):
    range = [get_class('ClientGoal')]


class hasActualClientState(ObjectProperty):
    range = [get_class('ClientState')]


class hasDesiredClientState(ObjectProperty):
    range = [get_class('ClientState')]


class inducesNeed(ObjectProperty):
    range = [get_class('Need')]


class hasDeadline(ObjectProperty):
    range = [time.DateTimeDescription]


class hasSubGoal(ObjectProperty):
    range = [get_class('ClientGoal')]


class hasTemporalHorizon(DataProperty):
    range = [str]


class affectsRisk(ObjectProperty):
    range = [get_class('Risk')]


class hasRiskFactor(ObjectProperty):
    range = [get_class('RiskFactor')]


class hasLikelihoodScore(DataProperty):
    range = [str]


class inducesCommunityRisk(ObjectProperty):
    range = [get_class('CommunityRisk')]


class ofClient(ObjectProperty):
    range = [get_class('Client')]


class hasNeedSatisfier(ObjectProperty):
    range = [get_class('NeedSatisfier')]


class hasImportance(DataProperty):
    range = [str]


class isExpressed(DataProperty):
    range = [bool]


class isNormative(DataProperty):
    range = [bool]


class hasNeedType(DataProperty):
    range = [str]


class hasChangeType(DataProperty):
    range = [str]


class hasFeature(ObjectProperty):
    range = [get_class('ClientFeature')]


class forNeed(ObjectProperty):
    range = [get_class('Need')]


class changes(ObjectProperty):
    range = [iso21972.Feature]


# class hasType(DataProperty):
#     range = [str]
# TODO: hasType cannot be both data property and object property

class hasImpact(DataProperty):
    range = [str]


class affectsClientState(ObjectProperty):
    range = [get_class('ClientState')]


# class hasDescription(DataProperty):
#     range = [str]

class hasCatchmentArea(ObjectProperty):
    range = [get_class('CL_CatchmentArea')]


class performs(ObjectProperty):
    range = [cids.Activity]


class providesSatisfier(ObjectProperty):
    range = [get_class('NeedSatisfier')]


class hasSatisfierType(DataProperty): pass
