from django import forms
from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.productid = kwargs.pop('productid', None)
        self.customerid = kwargs.pop('customerid', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.productid = self.productid
        comment.customerid = self.customerid
        comment.save()
        return comment
    class Meta:
        model = Comment
        fields = ['content', 'rating',]
        