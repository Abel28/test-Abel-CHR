# Generated by Django 4.0 on 2023-02-16 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('empty_slots', models.IntegerField(verbose_name='Slots')),
                ('free_bikes', models.IntegerField(verbose_name='Slots')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Stations',
        ),
    ]
