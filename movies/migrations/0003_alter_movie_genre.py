# Generated by Django 5.1.5 on 2025-02-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="genre",
            field=models.CharField(max_length=255),
        ),
    ]
