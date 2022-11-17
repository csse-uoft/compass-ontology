import time
from datetime import date

prev = time.time()

from owlready2 import *

compass_onto = default_world.get_ontology("http://helpseeker.co/compass#")

# Load ontologies
default_world.get_ontology('https://csse-uoft.github.io/ontologies/time.rdf').load()
default_world.get_ontology('https://csse-uoft.github.io/ontologies/geosparql.owl').load()
# default_world.get_ontology('./ontologies/Time.owl').load(load_all_properties=False)
cids_onto = default_world.get_ontology("http://ontology.eil.utoronto.ca/cids/cids.owl").load(load_all_properties=False)
# cids_onto = default_world.get_ontology("./ontologies/cids.owl").load(load_all_properties=False)
# act_onto = default_world.get_ontology("http://ontology.eil.utoronto.ca/tove/activity.owl").load(
#     load_all_properties=False)
ic_onto = default_world.get_ontology("http://ontology.eil.utoronto.ca/tove/icontact.owl").load(
    load_all_properties=False)
schema_onto = default_world.get_ontology(
    "https://schema.org/docs/schemaorg.owl").load(
    load_all_properties=False)
cwrc_onto = default_world.get_ontology("http://sparql.cwrc.ca/ontologies/cwrc.owl").load(load_all_properties=False)
# foaf_onto = default_world.get_ontology("https://xmlns.com/foaf/spec/20140114.rdf").load(load_all_properties=False)
sur_onto = default_world.get_ontology("http://ontology.eil.utoronto.ca/Survey/survey.owl").load(load_all_properties=False)
# dqv_onto = default_world.get_ontology("https://www.w3.org/ns/dqv.rdf").load(load_all_properties=False)
act_50871 = default_world.get_ontology("http://ontology.eil.utoronto.ca/5087/1/Activity.owl").load(load_all_properties=False)
city_50872 = default_world.get_ontology("http://ontology.eil.utoronto.ca/5087/2/City.owl").load(load_all_properties=False)


compass_onto.imported_ontologies = [cids_onto, ic_onto, schema_onto, act_50871, sur_onto, city_50872]

# Ontology Metadata Namespaces
vann = default_world.get_namespace("http://purl.org/vocab/vann/")
dc = default_world.get_namespace("http://purl.org/dc/elements/1.1/")
cc = default_world.get_namespace("http://creativecommons.org/ns#")
dcterms = default_world.get_namespace("http://purl.org/dc/terms/")
owl = default_world.get_namespace("http://www.w3.org/2002/07/owl#")

# Ontology Metadata
vann.preferredNamespacePrefix[compass_onto.metadata] = ['cp']
vann.preferredNamespaceUri[compass_onto.metadata] = ['http://helpseeker.co/compass#']
dcterms.title[compass_onto.metadata] = ['Compass Ontology']
dcterms.description[compass_onto.metadata] = ["""
The Compass ontology contains
- Compass Project Client Ontology
- Compass Project Service Ontology
- Compass Project Need Ontology"""]

dcterms.issued[compass_onto.metadata] = ['January 27, 2022']
dcterms.modified[compass_onto.metadata] = [date.today().strftime("%B %d, %Y")]
owl.versionInfo[compass_onto.metadata] = ["""
Version 0 January 27, 2022: Initial creation."""]
cc.license[compass_onto.metadata] = ['http://creativecommons.org/licenses/by/3.0/']
dcterms.creator[compass_onto.metadata] = ['Mark S. Fox, msf@eil.utoronto.ca; Daniela Rosu, drosu@cs.toronto.edu; '
                                     'Bart Gajderowicz, bartg@mie.utoronto.ca; Dishu Lyu, lvds2000@gmail.com']


print('--------------------Loaded-------------------')

with compass_onto:
    import src.namespaces
    from src.code_lists import *
    from src.properties import *
    from src.classes import *
    compass_onto.save('./compass.owl')

    # Load some examples
    # from demo import *
    # compass_onto.save('./compass-with-examples.owl')


def print_performance():
    import time
    print(f'---total time {(time.time() - prev):.4f}s---')
    from owlready2.backend.sparql_client import SparqlClient

    print(
        f'---SPARQL query time {SparqlClient.total_sparql_time:.4f}s for {SparqlClient.total_sparql_queries} queries---')
    times = SparqlClient.function_times.items()
    times = sorted(times, key=lambda x: x[1], reverse=True)
    for fun_name, (ms, times) in times:
        print(f'{fun_name} x{times} {round(ms * 1000)}ms')

