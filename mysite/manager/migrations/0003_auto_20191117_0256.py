# Generated by Django 2.2.7 on 2019-11-17 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsessionform',
            name='advisor_name',
        ),
        migrations.RemoveField(
            model_name='newsessionform',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='newsessionform',
            name='project_name',
        ),
    ]
