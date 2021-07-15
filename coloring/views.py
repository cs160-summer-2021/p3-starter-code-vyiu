from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def explore(request):
    return render(request, 'coloring/explore.html')