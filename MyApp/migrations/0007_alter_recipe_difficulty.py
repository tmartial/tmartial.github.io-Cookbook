# Generated by Django 4.1.1 on 2022-11-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0006_alter_recipe_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="difficulty",
            field=models.CharField(
                choices=[
                    ("easy", "Available to borrow"),
                    ("medium", "Borrowed by someone"),
                    ("difficult", "Archived - not available anymore"),
                ],
                help_text="Difficulty of this recipe",
                max_length=32,
            ),
        ),
    ]