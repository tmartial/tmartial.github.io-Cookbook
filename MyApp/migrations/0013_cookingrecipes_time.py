# Generated by Django 4.1.1 on 2022-11-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0012_cookingrecipes_delete_recipe"),
    ]

    operations = [
        migrations.AddField(
            model_name="cookingrecipes",
            name="time",
            field=models.PositiveIntegerField(
                default=30, help_text="Time to do this recipe in minutes"
            ),
        ),
    ]
