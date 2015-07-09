from django.forms import ModelForm
from .models import BlogComment

class CommentForm(ModelForm):

    class Meta:
        model = BlogComment
        fields = ('comment',)

    def is_valid(self):
        return True