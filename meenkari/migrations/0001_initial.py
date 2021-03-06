# Generated by Django 3.0.8 on 2020-07-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(blank=True, max_length=127)),
                ('game_name', models.CharField(default='Unnamed Game', max_length=32)),
                ('game_status', models.CharField(choices=[('open', 'open'), ('over', 'over'), ('left', 'left')], default='open', max_length=10)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('lastmodify_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('player_11', models.CharField(blank=True, max_length=32)),
                ('player_11_image', models.URLField(blank=True, max_length=300)),
                ('player_12', models.CharField(blank=True, max_length=32)),
                ('player_12_image', models.URLField(blank=True, max_length=300)),
                ('player_13', models.CharField(blank=True, max_length=32)),
                ('player_13_image', models.URLField(blank=True, max_length=300)),
                ('player_21', models.CharField(blank=True, max_length=32)),
                ('player_21_image', models.URLField(blank=True, max_length=300)),
                ('player_22', models.CharField(blank=True, max_length=32)),
                ('player_22_image', models.URLField(blank=True, max_length=300)),
                ('player_23', models.CharField(blank=True, max_length=32)),
                ('player_23_image', models.URLField(blank=True, max_length=300)),
                ('log', models.TextField(blank=True)),
                ('player_11_hand', models.TextField(blank=True)),
                ('player_12_hand', models.TextField(blank=True)),
                ('player_13_hand', models.TextField(blank=True)),
                ('player_21_hand', models.TextField(blank=True)),
                ('player_22_hand', models.TextField(blank=True)),
                ('player_23_hand', models.TextField(blank=True)),
                ('team_1_status', models.CharField(blank=True, max_length=40)),
                ('team_2_status', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
