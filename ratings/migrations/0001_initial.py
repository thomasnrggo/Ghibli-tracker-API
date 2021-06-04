# Generated by Django 3.2.3 on 2021-06-04 05:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('show_movies', '0009_auto_20210604_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('emoji_rating', models.IntegerField()),
                ('star_rating', models.IntegerField()),
                ('watched', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_movies.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_movies.profiles')),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
