# Generated by Django 4.1.1 on 2022-11-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="URL",
            field=models.URLField(help_text="URL wikipedia of the recipe"),
        ),
    ]