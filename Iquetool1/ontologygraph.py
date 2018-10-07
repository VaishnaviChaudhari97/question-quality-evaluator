from owlready2 import *
import networkx as nx

onto = get_ontology("file://final.owl").load()
g = nx.DiGraph()
color_map = []
owl = input("Enter owl file name : ")

print("--- CONCEPTS ---")
concept = list(onto.classes())
concepts = []
for i in range(len(concept)):
    concepts += str(concept[i]).split('.')
for i in concepts:
    concepts.remove(owl)
for i in range(len(concepts)):
    print(concepts[i])
    g.add_node(concepts[i])
    color_map.append('white')

print("\n--- RELATIONS ---")
weight = list(onto.object_properties())
weights = []
for i in range(len(weight)):
    weights += str(weight[i]).split('.')
for i in weights:
    weights.remove(owl)
for i in range(len(weights)):
    print(weights[i])

print("\n--- SUBCLASSES OF ---")
for x in range(len(concept)):
    subclass = list(concept[x].subclasses())

    if len(subclass) > 0:
        subclasses = []
        print("\n", concepts[x], "->")
        for i in range(len(subclass)):
            subclasses += str(subclass[i]).split('.')
        for i in subclasses:
            subclasses.remove(owl)
        for y in range(len(subclasses)):
            print("\t", subclasses[y])
            g.add_edge(concepts[x], subclasses[y])

