# Generated by Django 2.2 on 2022-10-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user_auth_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_auth',
            name='password',
            field=models.CharField(default='', max_length=150),
        ),
    ]
