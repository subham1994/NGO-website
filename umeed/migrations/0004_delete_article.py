# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umeed', '0003_umeednews'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
