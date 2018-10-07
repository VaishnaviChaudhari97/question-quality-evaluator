from django.shortcuts import render, redirect, HttpResponse
from .forms import DocumentForm

#def index(request):
#    return render(request, 'ontology/accept.html')


def accept(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'ontology/accept.html', {'form': form})


def details(request):
    #f = request.FILES('los').read()
    #f.close()
    #return HttpResponse(f, content_type="text/plain")
    return render(request, 'ontology/details.html')
