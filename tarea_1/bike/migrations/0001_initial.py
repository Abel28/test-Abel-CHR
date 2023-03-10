# Generated by Django 4.0 on 2023-02-18 13:33

from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('empty_slots', models.IntegerField(verbose_name='Slots')),
                ('free_bikes', models.IntegerField(blank=True, null=True, verbose_name='Free Bikes')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('timestamp', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('ebikes', models.IntegerField(blank=True, null=True)),
                ('has_ebikes', models.BooleanField(blank=True, null=True)),
                ('last_updated', models.CharField(blank=True, max_length=200, null=True)),
                ('normal_bikes', models.IntegerField(blank=True, null=True)),
                ('payment', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('key', 'Tarjeta'), ('transitcard', 'Tarjeta de Transito'), ('creditcard', 'Tarjeta de Crédito'), ('phone', 'Teléfono Movil')], max_length=32, null=True)),
                ('post_code', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('renting', models.IntegerField(blank=True, null=True)),
                ('returning', models.IntegerField(blank=True, null=True)),
                ('slots', models.IntegerField(blank=True, null=True)),
                ('uid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
