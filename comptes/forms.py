from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"username",
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"password",
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"username",
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"password",
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"confirm password",
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"email",
                "class": "form-control"
            }
        )
    )
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"username",
                
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"email",
                
            }
        )
    )
    is_admin = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"is_admin",

            }
        )
    )
    is_comptable = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"is_comptable",

            }
        )
    )
    is_grh = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"is_grh",

            }
        )
    )
    is_gstock = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"is_gstock",

            }
        )
    )
    is_anonimous = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "placeholder":"is_anonimous",

            }
        )
    )
    

    class Meta:
        model = User
        fields = ('username', 'email', 'is_admin', 'is_comptable','is_grh','is_gstock','is_anonimous')