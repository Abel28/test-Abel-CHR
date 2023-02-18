# Generated by Django 4.0 on 2023-02-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_alter_station_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='station',
            name='altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='ebikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='free_bikes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Slots'),
        ),
        migrations.AlterField(
            model_name='station',
            name='has_ebikes',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='last_updated',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='station',
            name='normal_bikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='post_code',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='renting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='returning',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='slots',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='uid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
