from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
#from sightings.models import Squirrel

#from sightings.forms import SquirrelForm

def index(request):
    #get 100 squirrels
    #return HttpResponse('Hello')

    return render(request, 'map/index.html', {})
# Create your views here.
