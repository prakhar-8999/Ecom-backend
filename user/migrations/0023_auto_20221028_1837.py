# Generated by Django 2.2 on 2022-10-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20221028_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_wallet',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
