from django.shortcuts import render

from sightings.models import Squirrel

def index(request):
    sight = Squirrel.objects.all()[:100]
    context = {
            'sightings':sight,
            }
    return render(request, 'map/index.html', context)
# Create your views here.
