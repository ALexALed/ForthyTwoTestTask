# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0005_auto_20141205_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybio',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
