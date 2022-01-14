from xml.dom.minidom import Comment
from django.forms import ModelForm
from .models import Comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['writer','content','post']
        