from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

	class Meta:
		model=User
		fields=['username', 'password1', 'password2']

class LoginForm(forms.Form):
    
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                'required':True
            }
        )
    )


class JobForm(forms.Form):
    title = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. Software Engineer'}))
    company = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. Google'}))
    type = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. Engineering'}))
    level = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. Entry, intermediate, or senior'}))
    address = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. 123 St'}))
    zipcode = forms.IntegerField()
    city = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. New York'}))
    state = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'e.g. NY'}))
    description = forms.CharField(
        widget = forms.Textarea(attrs={'placeholder': '...'}))
