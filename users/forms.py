from django import forms


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
