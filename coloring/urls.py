from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('index', views.index, name='index'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('explore', views.explore, name='explore'),
    path('compare', views.compare, name='compare'),
    path('home', views.home, name='home'),
    path('color', views.color, name='color'),
    path('studio', views.studio, name='studio'),
]
