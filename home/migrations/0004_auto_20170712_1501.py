# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0007_auto_20161016_1055'),
        ('home', '0003_auto_20170712_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('name', models.CharField(null=True, max_length=128, blank=True)),
                ('number', models.CharField(null=True, max_length=12, blank=True)),
                ('fase_test_cases', models.CharField(max_length=24, default='To Start', choices=[('To Start', 'To Start'), ('In development', 'In development'), ('Being reviewed', 'Being reviewed'), ('Ready for test', 'Ready for test'), ('Being tested', 'Being tested'), ('Tested, findings in progress', 'Tested, findings in progress'), ('Tested, findings solved', 'Tested, findings solved')])),
                ('notes', models.TextField()),
                ('process_model', filer.fields.image.FilerImageField(related_name='process_model', blank=True, null=True, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='cms.CMSPlugin', auto_created=True)),
                ('first_name', models.CharField(null=True, max_length=32, blank=True)),
                ('last_name', models.CharField(null=True, max_length=32, blank=True)),
                ('notes', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='process',
            name='testers',
            field=models.ManyToManyField(to='home.Tester'),
        ),
    ]
