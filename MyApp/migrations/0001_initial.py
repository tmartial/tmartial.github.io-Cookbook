# Generated by Django 4.1.1 on 2022-11-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="Name of the recipe", max_length=100),
                ),
                ("time", models.TimeField(help_text="Time to do this recipe")),
                (
                    "difficulty",
                    models.IntegerField(help_text="Difficulty of this recipe"),
                ),
                (
                    "image",
                    models.ImageField(help_text="Image of the recipe", upload_to=""),
                ),
                ("URL", models.URLField(help_text="URL of the recipe")),
                (
                    "origin",
                    models.CharField(help_text="Country of the recipe", max_length=100),
                ),
            ],
        ),
    ]