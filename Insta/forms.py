from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from Insta.models import InstaUser, Post

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ('username', 'email', 'profile_pic')


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["author"]
        