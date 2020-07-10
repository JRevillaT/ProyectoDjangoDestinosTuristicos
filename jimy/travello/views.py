from django.shortcuts import render
from .models import Destination
# Create your views here.

def vista(request):
    dests= Destination.objects.all()
    return render(request,'vista.html',{'dests':dests})


def index(request):
    dests= Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
