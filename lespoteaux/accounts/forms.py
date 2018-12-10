from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=190)
    email = forms.CharField(max_length=190)
    first_name = forms.CharField(max_length=50,
                                 required=False)
    last_name = forms.CharField(max_length=50,
                                required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)
