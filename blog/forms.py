from xml.dom.minidom import Comment
from django.forms import ModelForm
from .models import Comment
from mptt.forms import TreeNodeChoiceField


class CommentForm(ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['parent'].required = False
        self.fields['parent'].widget.attrs.update({'class':'d-none'})
    class Meta:
        model = Comment
        fields = ['content','parent']
        