# Generated by Django 2.2 on 2022-10-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221021_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp_verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('otp', models.IntegerField()),
            ],
        ),
    ]
