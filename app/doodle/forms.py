from django import forms
from doodle.models import Comment


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'cols': 80}),
        max_length=140,
        label='')

    class Meta:
        model = Comment
        fields = ['text']
        labels = False

class AddPost(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'cols': 70}),
        max_length=140,
        label='Added Post')

    class Meta:
        model = Comment
        fields = ['text']
        labels = False