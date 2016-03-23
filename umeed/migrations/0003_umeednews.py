# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umeed', '0002_umeedusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UmeedNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('umeeduser', models.ForeignKey(to='umeed.UmeedUsers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
