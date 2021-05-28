# Generated by Django 3.2.3 on 2021-05-20 06:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('original_title', models.CharField(max_length=32)),
                ('original_title_romanised', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=32)),
                ('release_date', models.IntegerField()),
                ('running_time', models.IntegerField()),
                ('rt_score', models.IntegerField()),
                ('music', models.CharField(max_length=32)),
                ('poster_url', models.URLField()),
            ],
        ),
    ]
