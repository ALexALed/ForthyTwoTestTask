# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0007_databaseevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='httprequestsave',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
