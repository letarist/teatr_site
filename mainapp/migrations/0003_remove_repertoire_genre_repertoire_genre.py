# Generated by Django 4.1.1 on 2022-09-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_remove_repertoire_artist_repertoire_artist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="repertoire",
            name="genre",
        ),
        migrations.AddField(
            model_name="repertoire",
            name="genre",
            field=models.ManyToManyField(to="mainapp.genre", verbose_name="Жанр"),
        ),
    ]
