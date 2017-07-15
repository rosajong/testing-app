from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Sprint


# Create your views here.
class SprintView(DetailView):
    model = Sprint
    template_name = 'sprint_page.html'
