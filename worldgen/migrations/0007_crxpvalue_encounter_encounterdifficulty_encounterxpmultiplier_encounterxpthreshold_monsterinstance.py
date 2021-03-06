# Generated by Django 3.2.3 on 2021-05-22 20:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0006_auto_20210521_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrXpValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('xp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EncounterDifficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='EncounterXpMultiplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_count_min', models.IntegerField(default=0)),
                ('monster_count_max', models.IntegerField(default=0)),
                ('multiplier', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='MonsterInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('current_hp', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.monster')),
            ],
        ),
        migrations.CreateModel(
            name='EncounterXpThreshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.encounterdifficulty')),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('level', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.encounterdifficulty')),
            ],
        ),
    ]
