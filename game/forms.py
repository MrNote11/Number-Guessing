from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class YourForm(forms.Form):
    number = forms.IntegerField(label='Enter a number')
    difficulty = forms.ChoiceField(
        choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
        label='Select difficulty'
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

DIFFICULTY_LEVELS = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

class WordInputForm(forms.Form):
    word = forms.CharField(max_length=100)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_LEVELS, required=True)
