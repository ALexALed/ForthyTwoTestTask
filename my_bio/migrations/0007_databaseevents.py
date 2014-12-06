# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0006_auto_20141205_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBaseEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signal', models.CharField(max_length=50, blank=True)),
                ('model', models.CharField(max_length=100, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
