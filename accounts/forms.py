from django import forms

# Forms for user to key in their user name and password
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)