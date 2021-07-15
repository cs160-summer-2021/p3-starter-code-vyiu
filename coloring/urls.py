from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),

    path('compare', views.compare, name='compare'),
    path('home', views.home, name='home'),
    path('landing', views.landing, name='landing'),
]
