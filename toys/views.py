from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Tag, Toy

# Create your views here.
def dashboard(request):
    return render(request, 'toys/dashboard.html', {'welcome_text': 'Welcome to all toys'})
    # return HttpResponse("Welcom to Alltoys")

def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__year=timezone.now().year)
    return render(request, 'toys/toys.html', {'toys': toys})