# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150708_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter_followers',
            field=models.BigIntegerField(default=-1),
        ),
    ]
