# Generated by Django 3.1.4 on 2021-04-12 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0003_auto_20210411_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matter',
            name='teacher',
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_classe', to='school.classe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
