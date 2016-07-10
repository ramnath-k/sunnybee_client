# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreReader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store', models.CharField(max_length=1024)),
                ('reader', models.CharField(max_length=1024)),
                ('status', models.IntegerField()),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
        ),
    ]
