from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=50)
    phone_number = models.TextField(max_length=25)
    linkedin_url = models.CharField(max_length=150)
    date_contacted = models.DateField('last contacted on', null=False)
    summary = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('connection_detail', kwargs={'connection_id': self.id})

class Skill(models.Model):
    name = models.CharField(max_length=25)
    completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(max_length=50, null=False)
    complete_by_date = models.DateField('Complete by', null=False)
    complete = models.BooleanField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=25)
    date = models.DateField()
    summary = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#search parameters will only be updated
class Search_Parameters(models.Model):
    job_titles = models.TextField(max_length=250, default="")
    job_boards = models.TextField(max_length=250, default="")
    keywords = models.TextField(max_length=250, default="")
    exclude_keywords = models.TextField(max_length=250, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='search_params')
