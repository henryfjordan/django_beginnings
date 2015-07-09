from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

# Create your views here.
from .models import BlogPost, BlogComment
from braces.views import LoginRequiredMixin
from .forms import CommentForm
from django_beginnings.users.models import User

class BlogList(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.all()

class BlogDetail(LoginRequiredMixin, DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.form = CommentForm(request.POST)
        if self.form.is_valid():
            comment = self.form.save(commit=False)
            #print(dir(self.object))
            comment.author = User.objects.get(username = self.request.user.username)
            comment.blogpost = self.get_object()
            comment.save()
            return super(BlogDetail, self).get(request, *args, **kwargs)
        else:
            return super(BlogDetail, self).post(request, *args, **kwargs)

class CommentList(ListView):
    model = BlogComment

