from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from .models import Squirrel

from .forms import SquirrelForm

#def index(request):
#    squirrels = 'Squirrel Tracker'
#    return render(request, 'squirrel/index.html')

#def map(request):
    #get 100 squirrels
#    return render(request,'squirrel/map.html')

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    ##squirrel = Squirrel.objects.get(Unique_Squirrel_ID=squirrel_id)
    context = {
            'squirrel': squirrels,
    }

    return render(request, 'sightings/stats.html', context)

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save
            form.save()
            return HttpResponse('Success! Your attemp to add a new sighting is Success!')
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    elif request.method == "GET":
        form = SquirrelForm()
        context = {
                'form': form,
        }
        
    return render(request, 'sightings/add.html', context) 


# Create your views here.
