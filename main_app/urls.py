from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('todos/', views.todos, name='todos'),
    path('connections/', views.connections_index, name='connections_index'),
    path('connections/<int:connection_id>', views.connections_detail, name='connections_detail'),
    path('events/', views.events, name='events'),
    path('skills/', views.skills, name='skills'),
    path('search_parameters/', views.search_parameters, name='search_parameters'),
    path('accounts/signup', views.signup, name='signup'),
]
