from django.shortcuts import render

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    
    return render(request, 'squirrel/index.html', {})

# Create your views here.
