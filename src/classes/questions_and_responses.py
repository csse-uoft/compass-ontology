from owlready2 import *
from src.namespaces import compass, cids, schema_old, tove_organization, sur, dqv, qb, dcterms
from src.utils import get_class


class Interview(sur.Survey):
    label = 'Interview'
    is_a = [
        compass.hasInterviewer.min(1, schema_old.Person),
        compass.dataCollector.exactly(1, schema_old.Person),
    ]


dcterms.description[Interview] = """
The Interview class defines the interview that is conducted between an interviewer and an interviewee. It is a subclass of the sur:Survey class. It has the following properties:
•	hasInterviewer: the person conducting the interview
•	dataCollector: a person collecting data of the interview
"""


class Estimate(sur.Question_Answer):
    label = 'Estimate'
    is_a = [
        # Has problem with
        # dqv.computedOn.only(qb.Dataset),
        compass.isEstimateOf.only(cids.Indicator)
    ]


dcterms.description[Estimate] = """
The Estimate is an extension of the survey approximate answer about an indicator, based on information in some dataset.
•	dqv:computedOn: the dataset from which the estimate is made (TBU)
•	isEstimateOf: the value this estimate is of

"""


class Computation(sur.Question_Answer):
    label = 'Computation'
    is_a = [
        # Has problem with
        # dqv.computedOn.only(qb.Dataset),
        compass.isComputationOf.only(cids.Indicator)
    ]


dcterms.description[Computation] = """
A Computation is an exact answer about an indicator, based on information in some dataset.
•	dqv:computedOn: the dataset from which the computation is made (TBU)
•	isComputationOf: the property the computation is of
"""
