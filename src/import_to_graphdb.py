from owlready2 import *

# STEPS to export the BRF file:
# 1. Make sure the repository is created and emptied
# 2. Make sure the sparql endpoint and username+password is correct
# 3. Go to https://compass.project.urbandatacentre.ca/graphs , Click "Export repository" and choose "Binary RDF".

default_world.set_backend('sparql-endpoint', endpoint="https://compass.project.urbandatacentre.ca/repositories/ontologies", username=None, password=None)
compass_onto = default_world.get_ontology("https://github.com/csse-uoft/compass-ontology/releases/download/latest/compass.owl").load()
