# Generated by Django 2.2 on 2022-10-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_left_pannel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_auth',
            name='Phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='user_auth',
            name='gst_num',
            field=models.CharField(default='', max_length=20),
        ),
    ]
