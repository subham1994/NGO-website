# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umeed', '0004_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersPayment',
            fields=[
                ('paymentId', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('amount', models.IntegerField()),
                ('paydate', models.DateTimeField(verbose_name=b'date paid')),
                ('hasdue', models.BooleanField(default=False)),
                ('umeeduser', models.ForeignKey(to='umeed.UmeedUsers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
