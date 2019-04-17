from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
import json
from . import extraction
from .forms import UserForm


def index(request):
    return render(request, 'ontology/index.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'ontology/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'ontology/home.html')

        return render(request, self.template_name, {'form': form})


def home(request):
    return render(request, 'ontology/home.html')


def documentation(request):
    return render(request, 'ontology/documentation.html')


def contact(request):
    return render(request, 'ontology/contact.html')


def ontologies(request):
    return render(request, 'ontology/ontologies.html')


def accept(request):
    return render(request, 'ontology/accept.html')


def relations(request):
    with request.FILES["concepts"] as f:
        nodes = f.read().decode("utf-8").splitlines()
        nodes = list(dict.fromkeys(nodes))
        nodes = list(filter(None, nodes))
        nodes = [name for name in nodes if name.strip()]
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