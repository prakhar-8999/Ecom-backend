# Generated by Django 2.2 on 2022-10-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_otp_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_auth',
            name='Name',
            field=models.CharField(default='', max_length=10),
        ),
    ]