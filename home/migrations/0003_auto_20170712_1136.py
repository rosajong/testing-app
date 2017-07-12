# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170709_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='sprint_number',
            field=models.CharField(max_length=16, default='1', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('Real Life Sprint', 'Real Life Sprint')]),
        ),
    ]
