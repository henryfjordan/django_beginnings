# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    def __unicode__(self):
        return self.username

    twitter_followers = models.BigIntegerField(default=0)
    instagram_followers = models.BigIntegerField(default=0)

    def get_total_followers(self):
        return self.twitter_followers + self.instagram_followers

