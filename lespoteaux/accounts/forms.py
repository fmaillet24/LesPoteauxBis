from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.CharField(label="Email", max_length=190)
    first_name = forms.CharField(label="First Name", max_length=50,
                                 required=False)
    last_name = forms.CharField(label="Last Name", max_length=50,
                                required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(label="Confirm", widget=forms.PasswordInput)
