# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20151107_1506'),
    ]

    operations = [
        migrations.DeleteModel(
            name='choices',
        ),
        migrations.AlterField(
            model_name='queueentry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 15, 6, 34, 83109)),
        ),
    ]
