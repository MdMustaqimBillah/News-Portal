from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from AuthorLoginApp.models import User

# Creating my forms here.

class SignupForm(UserCreationForm):
     email = forms.EmailField(
         label ='Email',
         widget=forms.TextInput(attrs={'placeholder':'Enter your email address'}))
     password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}),
    )
     password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}),
    )
     class Meta:
        model = User
        fields = ('email',)




class Authentication_Form(AuthenticationForm):
    username = forms.EmailField(
        widget= forms.EmailInput(attrs={'placeholder':'Enter your email address'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}),
    )
    class Meta:
        model = User
        fields = ['username']


class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField(
        widget= forms.EmailInput(attrs={'placeholder':'Enter your new email address'}),
    )
    class Meta:
        model = User
        fields = ['email']
