from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Bienvenido a Fayticell - Tu servicio tecnico de confianza.")
