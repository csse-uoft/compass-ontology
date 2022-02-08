from owlready2 import *

compass = default_world.get_ontology("http://ontology.eil.utoronto.ca/Compass/compass#")
schema = default_world.get_namespace("https://schema.org/")
schema_old = default_world.get_namespace("http://schema.org/")
tove_act = default_world.get_namespace("http://ontology.eil.utoronto.ca/tove/activity#")
tove_organization = default_world.get_namespace("http://ontology.eil.utoronto.ca/tove/organization#")
cids = default_world.get_namespace("http://ontology.eil.utoronto.ca/cids/cids#")
dcat = default_world.get_namespace("http://www.w3.org/ns/dcat#")
foaf = default_world.get_namespace("http://xmlns.com/foaf/0.1/")
ic = default_world.get_namespace("http://ontology.eil.utoronto.ca/tove/icontact#")
owl = default_world.get_namespace("http://www.w3.org/2002/07/owl#")
rdfs = default_world.get_namespace("http://www.w3.org/2000/01/rdf-schema#")
time = default_world.get_namespace("http://www.w3.org/2006/time#")
iso21972 = default_world.get_namespace("http://ontology.eil.utoronto.ca/ISO21972/iso21972#")
oep = default_world.get_namespace("http://www.w3.org/2001/sw/BestPractices/OEP/SimplePartWhole/part.owl#")
sur = default_world.get_namespace("http://ontology.eil.utoronto.ca/tove/survey#")
dqv = default_world.get_namespace("http://www.w3.org/ns/dqv#")
qb = default_world.get_namespace("http://purl.org/linked-data/cube#")
xsd = default_world.get_namespace("http://www.w3.org/2001/XMLSchema#")
dcterms = default_world.get_namespace("http://purl.org/dc/terms/")
act_50871 = default_world.get_namespace("http://ontology.eil.utoronto.ca/5087/1/Activity")
city_50872 = default_world.get_namespace("http://ontology.eil.utoronto.ca/5087/2/City")


# Short Names
i72 = iso21972
act = tove_act
org = tove_organization
