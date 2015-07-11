# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_twitter_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='twitter_followers',
            field=models.BigIntegerField(default=0),
        ),
    ]
