from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import BlogPost


class BlogList(ListView):
    model = BlogPost

class BlogDetail(DetailView):
    model = BlogPost