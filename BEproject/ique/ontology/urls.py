from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^home/', views.home, name='home'),

    url(r'^ontologies/', views.ontologies, name='ontologies'),

    #Accept concepts in syllabus from user
    url(r'^accept/', views.accept, name='accept'),

    #Make ontology
    url(r'^relations/', views.relations, name='relations'),

    url(r'^graph/', views.graph, name='graph'),

    #Accept LOs and Questions files
    url(r'^files/', views.files, name='files'),

    #Evaluate the question quality
    url(r'^evaluation/', views.evaluation, name='evaluation'),

    #
    url(r'^details/', views.details, name='details')
    ]
