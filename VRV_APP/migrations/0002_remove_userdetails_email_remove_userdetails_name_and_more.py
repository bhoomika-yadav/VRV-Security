# Generated by Django 5.0.1 on 2024-12-03 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VRV_APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='password',
        ),
    ]
