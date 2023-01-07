from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def funky(request):
    response = """
    <h1> funky function sample </h1>
    """
    return HttpResponse(response)