# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_bio', '0004_mybio_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybio',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photo/', blank=True),
            preserve_default=True,
        ),
    ]
