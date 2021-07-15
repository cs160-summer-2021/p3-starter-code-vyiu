from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def compare(request):
    return render(request, 'coloring/compare.html')

def home(request):
    return render(request, 'coloring/home.html')

def explore(request):
    return render(request, 'coloring/explore.html')

def color(request):
    return render(request, 'coloring/color.html')

def studio(request):
    return render(request, 'coloring/studio.html')
