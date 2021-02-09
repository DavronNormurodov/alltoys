from django.http import HttpResponse
from django.shortcuts import render
from .models import Tag, Toy

# Create your views here.
def dashboard(request):
    return render(request, 'toys/dashboard.html', {'welcome_text': 'Welcome to all toys'})
    # return HttpResponse("Welcom to Alltoys")

def get_toys(request):
    toys = Toy.objects.all()
    return render(request, 'toys/toys.html', {'toys': toys})