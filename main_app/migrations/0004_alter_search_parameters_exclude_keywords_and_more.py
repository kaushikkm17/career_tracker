# Generated by Django 4.1.6 on 2023-02-12 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_connection_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_parameters',
            name='exclude_keywords',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='search_parameters',
            name='job_boards',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='search_parameters',
            name='job_titles',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='search_parameters',
            name='keywords',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='search_parameters',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
