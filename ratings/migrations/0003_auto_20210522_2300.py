# Generated by Django 3.2.3 on 2021-05-23 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_alter_ratings_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='user_id',
            new_name='user',
        ),
    ]