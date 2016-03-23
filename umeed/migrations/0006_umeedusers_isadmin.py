# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umeed', '0005_userspayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='umeedusers',
            name='isAdmin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
