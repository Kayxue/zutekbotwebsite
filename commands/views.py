from django.shortcuts import render
from django.views.generic import *

# Create your views here.

class AllCommand(TemplateView):
    template_name = "allcommand.html"
