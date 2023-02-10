from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('todos/', views.todos_index, name='todos_index'),
    path('todos/<int:todo_id>/', views.TodoDetail.as_view(), name='todos_detail'),
    path('todos/create', views.TodoCreate.as_view(), name='todos_create'),
    path('todos/<int:todo_id>/update', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:todo_id>/delete', views.TodoDelete.as_view(), name='todos_delete'),
    path('connections/', views.connections_index, name='connections_index'),
    path('connections/<int:connection_id>', views.ConnectionDetail.as_view(), name='connections_detail'),
    path('connections/create', views.ConnectionCreate.as_view(), name='connections_create'),
    path('connections/<int:todo_id>/update', views.ConnectionUpdate.as_view(), name='connections_update'),
    path('connections/<int:todo_id>/delete', views.ConnectionDelete.as_view(), name='connections_delete'),
    path('events/', views.events_index, name='events_index'),
    path('events/<int:connection_id>', views.EventDetail.as_view(), name='events_detail'),
    path('events/create', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:todo_id>/update', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:todo_id>/delete', views.EventDelete.as_view(), name='events_delete'),
    path('skills/', views.skills_index, name='skills_index'),
    path('skills/<int:connection_id>', views.SkillDetail.as_view(), name='skills_detail'),
    path('skills/create', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:todo_id>/update', views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:todo_id>/delete', views.SkillDelete.as_view(), name='skills_delete'),
    path('search_parameters/', views.search_parameters_index, name='search_parameters_index'),
    path('search_parameters/create', views.SearchParametersCreate.as_view(), name='search_parameters_create'),
    path('search_parameters/<int:todo_id>/update', views.SearchParametersUpdate.as_view(), name='search_parameters_update'),
    path('accounts/signup', views.signup, name='signup'),
]
