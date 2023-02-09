from django.contrib import admin

# Register your models here.
from .models import Connection, Skill, Todo, Event, Search_Parameters
admin.site.register(Connection)
admin.site.register(Skill)
admin.site.register(Todo)
admin.site.register(Event)
admin.site.register(Search_Parameters)