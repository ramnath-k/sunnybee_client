# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_id', models.CharField(max_length=1024)),
                ('antenna', models.CharField(max_length=1024)),
                ('reader', models.CharField(max_length=1024)),
                ('status', models.IntegerField()),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
        ),
    ]
