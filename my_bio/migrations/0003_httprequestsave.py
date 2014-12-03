# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0002_auto_20141203_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpRequestSave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('http_request', models.CharField(max_length=300)),
                ('remote_addr', models.IPAddressField(blank=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
