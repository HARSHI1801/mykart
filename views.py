
from django.shortcuts import render
from django.http import HttpResponse



def index(request):
     return render(request, 'myshop/index.html')

def about(request):
     return HttpResponse("WE ARE AT ABOUT")

def contact(request):
     return HttpResponse("WE ARE AT CONTACT")

def tracker(request):
     return HttpResponse("WE ARE AT TRACKING")

def search(request):
     return HttpResponse("WE ARE AT search")

def productview(request):
     return HttpResponse("WE ARE AT pv")

def checkout(request):
     return HttpResponse("WE ARE AT couT")


