from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
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
def todos_index(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos.html', {'todos': todos})

@login_required
def connections_index(request):
    connections = Connection.objects.filter(user=request.user)
    return render(request, 'connections/index.html', {'connections': connections})


@login_required
def events_index(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/index.html', {'events': events})

@login_required
def skills_index(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills/index.html', {'skills': skills})

@login_required
def search_parameters_index(request):
    search_parameters = Search_Parameters.objects.filter(user=request.user)
    return render(request, 'search_parameters/index.html', {'search_parameters': search_parameters})
    

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
    success_url = '/todos/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['name', 'complete_by_date', 'complete']

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todos/'

class ConnectionCreate(LoginRequiredMixin, CreateView):
    model = Connection
    fields = ['name', 'email', 'phone_number', 'linkedin_url', 'date_contacted', 'summary']
    success_url = '/connections/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ConnectionDetail(LoginRequiredMixin, DetailView):
    model = Connection

class ConnectionUpdate(LoginRequiredMixin, UpdateView):
    model = Connection
    fields = ['name', 'email', 'phone_number', 'linkedin_url', 'date_contacted', 'summary']

class ConnectionDelete(LoginRequiredMixin, DeleteView):
    model = Connection
    success_url = '/connections/'

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'date', 'summary']
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'date', 'summary']

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['name', 'completed']
    success_url = '/skills/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SkillDetail(LoginRequiredMixin, DetailView):
    model = Skill

class SkillUpdate(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['name', 'completed']

class SkillDelete(LoginRequiredMixin, DeleteView):
    model = Skill
    success_url = '/skills/'

#search parameters will only be able to be created once then only updated
class SearchParametersCreate(LoginRequiredMixin, CreateView):
    model = Search_Parameters
    fields = ['job_titles', 'job_boards', 'keywords', 'exclude_keywords']
    success_url = '/search_parameters/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SearchParametersUpdate(LoginRequiredMixin, UpdateView):
    model = Search_Parameters
    fields = ['job_titles', 'job_boards', 'keywords', 'exclude_keywords']

