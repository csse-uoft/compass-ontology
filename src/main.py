import time
from datetime import date

prev = time.time()

from owlready2 import *

compass_onto = default_world.get_ontology("http://helpseeker.co/compass#")

# Load ontologies
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
foaf_onto = default_world.get_ontology("http://xmlns.com/foaf/spec/index.rdf").load(load_all_properties=False)
sur_onto = default_world.get_ontology("./ontologies/survey.owl").load(load_all_properties=False)
# dqv_onto = default_world.get_ontology("https://www.w3.org/ns/dqv.rdf").load(load_all_properties=False)
act_50871 = default_world.get_ontology("http://ontology.eil.utoronto.ca/5087/1/Activity.owl").load(load_all_properties=False)
city_50872 = default_world.get_ontology("http://ontology.eil.utoronto.ca/5087/2/City.owl").load(load_all_properties=False)

sur_onto.set_location('http://ontology.eil.utoronto.ca/tove/survey.owl')

compass_onto.imported_ontologies = [cids_onto, ic_onto, schema_onto, act_50871, sur_onto, city_50872]

# Ontology Metadata
compass_onto.metadata.preferredNamespacePrefix.append('cp')
compass_onto.metadata.preferredNamespaceUri.append('http://helpseeker.co/compass#')
compass_onto.metadata.title.append('Compass Ontology')
compass_onto.metadata.description.append("""
The Compass ontology contains
- Compass Project Client Ontology
- Compass Project Service Ontology
- Compass Project Need Ontology""")
compass_onto.metadata.issued.append('January 27, 2022')
compass_onto.metadata.modified.append(date.today().strftime("%B %d, %Y"))
compass_onto.metadata.versionInfo.append("""
Version 0 January 27, 2022: Initial creation.""")
compass_onto.metadata.license.append('http://creativecommons.org/licenses/by/3.0/')
compass_onto.metadata.creator.append('Mark S. Fox, msf@eil.utoronto.ca; Daniela Rosu, drosu@cs.toronto.edu; '
                                     'Bart Gajderowicz, bartg@mie.utoronto.ca; Dishu Lyu, lvds2000@gmail.com')


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

