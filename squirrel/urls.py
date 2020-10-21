from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns = [
    path('', views.home, name='home'),
    path('map',views.map, name='map'),
    path('sightings', views.sightings, name='index'),
    path('stats', views.stats, name='stats'),
    path('sightings/add', views.add, name='add'),

]

