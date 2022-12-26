from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        self.customer = kwargs.pop('customer', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.product = self.product
        comment.customer = self.customer
        comment.save()
        return comment

    class Meta:
        model = Comment
        fields = ['content', 'rating', ]
