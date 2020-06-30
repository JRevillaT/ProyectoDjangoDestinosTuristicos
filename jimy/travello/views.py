from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name = 'PeruCity'
    dest1.desc = 'La cuna del sillar y el adobo'
    dest1.price = 500
    dest1.img='destination_1.jpg'
    dest1.offer= True

    dest2=Destination()
    dest2.name = 'Ancash'
    dest2.desc = 'Aqui tenemos el nevado Huascaran'
    dest2.price = 500
    dest2.img='destination_2.jpg'
    dest2.offer= False

    dest3=Destination()
    dest3.name = 'Cuzco'
    dest3.desc = 'El ombligo del mundo, Macchu Picchu'
    dest3.price = 450
    dest3.img='destination_3.jpg'
    dest3.offer= True

    dests=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})