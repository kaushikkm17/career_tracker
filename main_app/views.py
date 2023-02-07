from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def todo(request):
    return render(request, 'todo.html')
    
def connections_index(request):
    return render(request, 'connections/index.html')

def connections_detail(request):
    return render(request, 'connections/detail.html')

def events(request):
    return render(request, 'events.html')

def skills(request):
    return render(request, 'skills.html')

def search_parameters(request):
    return render(request, 'search_parameters.html')


