# Generated by Django 3.1.4 on 2021-04-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210411_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='born_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]