# Generated by Django 4.0 on 2023-02-18 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seia', '0003_alter_proyects_fecha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proyects',
            new_name='Project',
        ),
    ]
