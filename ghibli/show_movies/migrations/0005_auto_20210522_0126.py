# Generated by Django 3.2.3 on 2021-05-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_movies', '0004_alter_movies_cover_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='wiki_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='poster_url',
            field=models.URLField(),
        ),
    ]