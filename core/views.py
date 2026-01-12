from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "core/home.html")

def contacto(request):
    return HttpResponse("Página de contacto - Aquí irán los datos del técnico")

