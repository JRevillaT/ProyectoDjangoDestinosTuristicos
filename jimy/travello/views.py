from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name = 'PeruCity'
    dest1.desc = 'La cuna del sillar'
    return render(request,'index.html',{'dest1':dest1})