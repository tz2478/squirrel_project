from django.urls import path
from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.index, name='index'),
    #path('map',views.map, name='map'),
    #path('sightings', views.sightings, name='index'),
    path('stats', views.stats, name='stats'),
    path('add', views.add, name='add'),
    path('<squirrel_ID>/', views.update, name='update'),

]

