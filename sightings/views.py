from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse

from .models import Squirrel

from .forms import SquirrelForm

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

def stats(request):
    total = Squirrel.objects.all().count()
    adult_count = Squirrel.objects.filter(Age='Adult').count()
    primary_fur_color_count = Squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    location_count = Squirrel.objects.filter(Location='Ground Plane').count()
    running_count = Squirrel.objects.filter(Running='True').count()
    not_eating_count = Squirrel.objects.filter(Eating='False').count()
    context = {
            'total': total,
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
            form.save()
            return HttpResponse('Your attemp to add a new sighting is Successful!')
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    elif request.method == "GET":
        form = SquirrelForm()
        context = {
                'form': form,
        }
        
    return render(request, 'sightings/add.html', context) 

def update(request, squirrel_ID):
    obj = Squirrel.objects.filter(Unique_Squirrel_ID = squirrel_ID).first()

    if request.method == "POST":
        form = SquirrelForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponse('Your attemp to update a new sighting is Successful!')
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    elif request.method == "GET":
        form = SquirrelForm(instance = obj)
        context = {
                'form': form,
                'squirrel_ID': squirrel_ID,
        }

    return render(request, 'sightings/update.html', context)

# Create your views here.
