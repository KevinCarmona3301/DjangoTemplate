from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def display(request):
    return HttpResponse("<h1>Hello World</h1>")

def displayDate(request):
    date = datetime.datetime.now()
    return HttpResponse("<h1>La fecha y la hora es: " + str(date) + "</h1>")

def renderTemplate(request):
    return render(request, 'firstApp/informacionUsuario.html')

