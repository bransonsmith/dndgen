# Generated by Django 3.2.3 on 2021-05-23 22:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0007_crxpvalue_encounter_encounterdifficulty_encounterxpmultiplier_encounterxpthreshold_monsterinstance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('height', models.IntegerField(default=1)),
                ('width', models.IntegerField(default=1)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('height', models.IntegerField(default=1)),
                ('width', models.IntegerField(default=1)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('created', models.DateTimeField(verbose_name='Creation Time')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.environment')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.locationtype')),
            ],
        ),
        migrations.AddField(
            model_name='environment',
            name='environment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.environmenttype'),
        ),
        migrations.AddField(
            model_name='environment',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.region'),
        ),
    ]
