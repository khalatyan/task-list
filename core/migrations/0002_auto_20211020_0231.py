# Generated by Django 2.2 on 2021-10-19 18:31

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='picture',
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=core.models.content_file_name, verbose_name='Файл')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Task', verbose_name='Задача')),
            ],
            options={
                'verbose_name': 'файл задач',
                'verbose_name_plural': 'Файлы задач',
            },
        ),
    ]