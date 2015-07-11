# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin


from .forms import UserForm
from .models import User


import tweepy
from allauth.socialaccount.models import SocialAccount



class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_twitter_follower_count(self):
        auth = tweepy.OAuthHandler('08OKIFS5pnBFYULL8duPsTvkd', 'QvoNYSyTWsbzJLZiBFiUDn7U2rzb4ms2qLjfDLBmyl7So7PYa9')
        api = tweepy.API(auth)
        twitter_uid = SocialAccount.objects.filter(user_id=self.id, provider='twitter').first()
        return api.get_user(twitter_uid).followers_count




class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
