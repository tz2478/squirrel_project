from django.urls import path
from . import views

app_name = 'squirrel'

urlpatterns = [
    path('', views.home, name='home'),
    path('map',views.map, name='map'),
    path('sightings', views.sightings, name='sightings'),
    path('stats', views.stats, name='stats'),
    path('add', views.add, name='add'),

]

