"""Defines URL patterns for ase_site."""

from django.urls import path
from . import views

app_name = "ase_site"

urlpatterns = [
    #Home Page 
    path("", views.index, name="index"),

    #Search Results
    path("results/", views.results, name="results"),

    #Individual Posting Page
    path("results/<int:posting_id>/", views.posting, name="posting"), 

    #Add Job Posting
    path("new_post/", views.new_post, name="new_post"),
]
