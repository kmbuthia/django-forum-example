from django import forms
from .models import Post, Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={'rows': 5, 'placeholder': "What's on your mind?"}
            ),
            max_length=4000,
            help_text='The max length of this text is 4000 characters',
        )

    class Meta:
        model = Topic
        fields = ('subject', 'message')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message',)
