# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('birth_date', models.DateField(verbose_name='Date of birth', blank=True)),
                ('biography', models.TextField(verbose_name='Bio', blank=True)),
                ('contacts', models.TextField(verbose_name='Contacts', blank=True)),
                ('other_contacts', models.TextField(verbose_name='Other contacts', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
