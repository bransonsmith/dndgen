# Generated by Django 3.2.3 on 2021-05-24 00:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0008_auto_20210523_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='locationtype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
