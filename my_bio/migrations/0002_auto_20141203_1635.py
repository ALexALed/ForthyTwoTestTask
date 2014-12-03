# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mybio',
            name='contacts',
        ),
        migrations.AddField(
            model_name='mybio',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mybio',
            name='jabber',
            field=models.EmailField(max_length=75, null=True, verbose_name='Jabber', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mybio',
            name='skype',
            field=models.CharField(max_length=200, null=True, verbose_name='Skype', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybio',
            name='biography',
            field=models.TextField(null=True, verbose_name='Bio', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybio',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Date of birth', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mybio',
            name='other_contacts',
            field=models.TextField(null=True, verbose_name='Other contacts', blank=True),
            preserve_default=True,
        ),
    ]
