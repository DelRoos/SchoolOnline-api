# Generated by Django 3.1.4 on 2021-04-11 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210410_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='letter',
            new_name='num',
        ),
    ]