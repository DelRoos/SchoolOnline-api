# Generated by Django 3.2 on 2021-04-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
