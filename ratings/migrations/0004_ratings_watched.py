# Generated by Django 3.2.3 on 2021-05-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20210522_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]
