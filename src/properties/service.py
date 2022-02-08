from owlready2 import DataProperty, ObjectProperty
from src.namespaces import compass, cids, tove_organization, time, iso21972
from src.utils import get_class

class providedBy(ObjectProperty):
    pass

class hasCost(DataProperty):
    pass

class hasCommunityCharacteristic(ObjectProperty):
    pass

class hasNumber(DataProperty):
    pass

class hasSource(DataProperty):
    pass

class hasApplication(ObjectProperty):
    pass

class hasUserStakeholder(ObjectProperty):
    pass

class hasMetaData(DataProperty):
    pass

class forReferral(ObjectProperty): pass

class forService(ObjectProperty): pass

class hasFailureType(ObjectProperty): pass

class hasInterviewer(ObjectProperty): pass

class dataCollector(ObjectProperty): pass

class isEstimateOf(ObjectProperty): pass

class isComputationOf(ObjectProperty): pass
