# Generated by Django 3.2.3 on 2021-05-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_avatar_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='user', max_length=32),
            preserve_default=False,
        ),
    ]