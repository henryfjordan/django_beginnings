from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogComment

admin.site.register(BlogPost)
admin.site.register(BlogComment)