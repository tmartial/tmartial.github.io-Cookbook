# Generated by Django 4.1.1 on 2022-11-27 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0010_rename_time_recipe_timecooking"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="timecooking",
        ),
    ]
