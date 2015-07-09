from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from .models import BlogPost, BlogComment
from braces.views import LoginRequiredMixin

class BlogList(ListView):
    model = BlogPost

class BlogDetail(DetailView):
    model = BlogPost

class CommentList(ListView):
    model = BlogComment

class CommentForm(LoginRequiredMixin, CreateView):
    model = BlogComment
    success_url = "/"
    fields = ['comment',]