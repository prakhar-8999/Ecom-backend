# Generated by Django 2.2 on 2022-10-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_auth',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
