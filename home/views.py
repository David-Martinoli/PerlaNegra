"""Vistas para la aplicación home."""

from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    """Renderiza la página principal del sitio."""
    return render(request, 'home/index.html')
