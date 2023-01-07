from django.shortcuts import render
from django.views import View, generic
from django.urls import reverse, reverse_lazy

from gview.models import Cat


# Create your views here.
class CatListView(generic.ListView):
    model = Cat

class CatDetailView(generic.DetailView):
    model = Cat