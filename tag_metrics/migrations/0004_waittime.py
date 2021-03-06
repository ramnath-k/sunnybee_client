# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_metrics', '0003_crate'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wait_time', models.IntegerField()),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
        ),
    ]
