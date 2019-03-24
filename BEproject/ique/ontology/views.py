from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
import json
from . import extraction


def home(request):
    return render(request, 'ontology/home.html')


def ontologies(request):
    return render(request, 'ontology/ontologies.html')


def accept(request):
    return render(request, 'ontology/accept.html')


def relations(request):
    with request.FILES["concepts"] as f:
        nodes = f.read().decode("utf-8").splitlines()
    return render(request, 'ontology/relations.html', {'nodes': nodes})


def graph(request):
    return render(request, 'ontology/graph.html')


def files(request):
    return render(request, 'ontology/files.html')


def evaluation(request):
    lo = request.FILES["LO_file"].read().decode("utf-8").lower()
    qu = request.FILES["questions_file"].read().decode("utf-8").lower()

    lo_conc = extraction.get_concepts(lo)
    lo_cogn = extraction.get_cognitive(lo)
    for item1 in lo_cogn:
        for item2 in lo_conc:
            if item1["id"] == item2["id"]:
                item1.update(item2)

    qu_conc = extraction.get_concepts(qu)
    qu_cogn = extraction.get_cognitive(qu)
    for item1 in qu_cogn:
        for item2 in qu_conc:
            if item1["id"] == item2["id"]:
                item1.update(item2)

    final = { "los": lo_cogn, "questions": qu_cogn}
    #final1 = json.dumps(final)
    return render(request, 'ontology/evaluation.html', {'final': final})


def details(request):
        return render(request, 'ontology/details.html')