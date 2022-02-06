from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, Select, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import News, Comment


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password again', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'is_published', 'category', ]

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]
        widgets = {'comment': Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'write a comment...'})}
