from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from squirrel.models import Squirrel

from squirrel.forms import SquirrelForm

def index(request):
    #get 100 squirrels
    #return HttpResponse('Hello')

    return render(request, 'map/index.html', {})
# Create your views here.
