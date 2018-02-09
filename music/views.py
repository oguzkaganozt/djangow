# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


# TODO make great views !
def index(request):
    return HttpResponse("<b>Music Index<b>")

