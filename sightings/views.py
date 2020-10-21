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
    adult_count = Squirrel.objects.filter(Age='Adult').count()
    primary_fur_color_count = Squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    location_count = Squirrel.objects.filter(Location='Ground Plane').count()
    running_count = Squirrel.objects.filter(Running='True').count()
    not_eating_count = Squirrel.objects.filter(Eating='False').count()
    ##squirrel = Squirrel.objects.get(Unique_Squirrel_ID=squirrel_id)
    context = {
            'adult_count': adult_count,
            'primary_fur_color_count': primary_fur_color_count,
            'location_count': location_count,
            'running_count': running_count,
            'not_eating_count': not_eating_count,
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

def update(request):
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

    return render(request, 'sightings/update.html', context)

# Create your views here.
