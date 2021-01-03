from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are at the polls index")

def home(request, *args, **kwargs):
	return render(request, "homepage.html", {})