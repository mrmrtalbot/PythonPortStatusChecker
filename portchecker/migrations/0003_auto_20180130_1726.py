# Generated by Django 2.0.1 on 2018-01-30 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portchecker', '0002_auto_20180130_1424'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PortsStatus',
            new_name='Ports',
        ),
        migrations.RenameField(
            model_name='ports',
            old_name='port_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ports',
            old_name='port_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='ports',
            old_name='port_type',
            new_name='type',
        ),
    ]
