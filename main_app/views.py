from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Connection, Skill, Todo, Event, Search_Parameters

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def todo(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos})

@login_required
def connections_index(request):
    connections = Connection.objects.filter(user=request.user)
    return render(request, 'connections/index.html', {'connections': connections})

@login_required
def connections_detail(request):
    return render(request, 'connections/detail.html')

@login_required
def events(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events.html', {'events': events})

@login_required
def skills(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills.html', {'skills': skills})

@login_required
def search_parameters(request):
    search_parameters = Search_Parameters.objects.filter(user=request.user)
    return render(request, 'search_parameters.html', {'search_parameters': search_parameters})
    

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['name', 'complete_by_date', 'complete']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


