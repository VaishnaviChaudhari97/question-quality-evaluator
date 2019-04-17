from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    #First page
    url(r'^index/', views.index, name='index'),

    url(r'^register/', views.UserFormView.as_view(), name='register'),

    url(r'^home/', views.home, name='home'),

    url(r'^documentation/', views.documentation, name='documentation'),

    url(r'^contact/', views.contact, name='contact'),

    #List of exisiting ontologies
    url(r'^ontologies/', views.ontologies, name='ontologies'),

    #Accept concepts in syllabus from user
    url(r'^accept/', views.accept, name='accept'),

    #Make ontology
    url(r'^relations/', views.relations, name='relations'),

    #Grapgical representation of ontology
    url(r'^graph/', views.graph, name='graph'),

    #Accept LOs and Questions files
    url(r'^files/', views.files, name='files'),

    #Evaluate the question quality and its tabular representation
    url(r'^evaluation/', views.evaluation, name='evaluation'),

    #Mapped ontology and its graphical representation
    url(r'^details/', views.details, name='details')
    ]
