# Generated by Django 4.2 on 2024-01-05 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_auth", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="date_of_birth",
        ),
        migrations.RemoveField(
            model_name="user",
            name="description",
        ),
        migrations.RemoveField(
            model_name="user",
            name="gender",
        ),
    ]
