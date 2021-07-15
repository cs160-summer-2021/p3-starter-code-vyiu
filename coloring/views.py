from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def demo(request):
    return render(request, 'coloring/demo.html')


def compare(request):
    return render(request, 'coloring/compare.html')


def home(request):
    return render(request, 'coloring/home.html')

def landing(request):
    return render(request, 'coloring/landing.html')
