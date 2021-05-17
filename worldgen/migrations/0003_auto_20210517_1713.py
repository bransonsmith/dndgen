# Generated by Django 3.2.3 on 2021-05-17 17:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worldgen', '0002_artobject_artobjectgroup_artobjectgroupentry_artobjecttreasurehoardentry_coin_cointreasurehoardentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSignifigance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('attunement', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItemGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(default='', max_length=150)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItemInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('magic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magicitem')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
            ],
        ),
        migrations.CreateModel(
            name='TreasureHoardMagicItemRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('magic_item_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magicitemgroup')),
                ('treasure_hoard_roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.treasurehoardrolltable')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItemTreasureHoardEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('magic_item_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magiciteminstance')),
                ('treasure_hoard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.treasurehoard')),
            ],
        ),
        migrations.CreateModel(
            name='MagicItemGroupEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_dice', models.CharField(default='', max_length=100)),
                ('min_roll', models.IntegerField()),
                ('max_roll', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Time')),
                ('extra_group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_group', to='worldgen.magicitemgroup')),
                ('magic_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magicitem')),
                ('magic_item_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magicitemgroup')),
            ],
        ),
        migrations.AddField(
            model_name='magicitem',
            name='magic_item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.magicitemtype'),
        ),
        migrations.AddField(
            model_name='magicitem',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.rarity'),
        ),
        migrations.AddField(
            model_name='magicitem',
            name='signifigance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.itemsignifigance'),
        ),
        migrations.AddField(
            model_name='magicitem',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldgen.contentsource'),
        ),
    ]
