# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='ending_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='sprint',
            name='starting_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
