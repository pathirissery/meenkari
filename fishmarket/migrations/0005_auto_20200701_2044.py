# Generated by Django 3.0.7 on 2020-07-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishmarket', '0004_auto_20200701_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='team_1_status',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='game',
            name='team_2_status',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]