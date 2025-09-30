from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Checking job</h4>")
def about (request):
    return HttpResponse("<h4>My job</h4>")