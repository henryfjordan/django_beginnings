# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin


from .forms import UserForm
from .models import User


import tweepy
from instagram.client import InstagramAPI
from allauth.socialaccount.models import SocialAccount

def get_twitter_follower_count(user):
    auth = tweepy.OAuthHandler('08OKIFS5pnBFYULL8duPsTvkd', 'QvoNYSyTWsbzJLZiBFiUDn7U2rzb4ms2qLjfDLBmyl7So7PYa9')
    api = tweepy.API(auth)
    twitter_uid = SocialAccount.objects.filter(user_id=user.id, provider='twitter')[0].uid
    user.twitter_followers = api.get_user(twitter_uid).followers_count
    user.save()

def get_instagram_follower_count(user):
    api = InstagramAPI(client_id='13245ce01c854900a3a964b9bdd964c5', client_secret='ed11480527dc4f6d959bc2fde47d25da')
    instagram_uid = SocialAccount.objects.filter(user_id=user.id, provider='instagram')[0].uid
    user.instagram_followers = api.user(instagram_uid).counts['followed_by']
    user.save()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get(self, request, *args, **kwargs):
        get_twitter_follower_count(self.get_object())
        get_instagram_follower_count(self.get_object())
        return super(UserDetailView, self).get(request, *args, **kwargs)

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
