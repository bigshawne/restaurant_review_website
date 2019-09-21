from django import forms
from django.contrib.auth.models import User
import re


# Check if the email address is used
def email_check(email):
    # The website will only store the email address with lower case, so change the email to lower case to validate.
    email = email.lower()
    pattern = re.complie(r"\"?[-a-z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    email = forms.CharField(label="Email", )
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("Your username must be at least 6 characters long.")

        elif len(username) > 64:
            raise forms.ValidationError("Your username is too long.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("Username has existed.")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("Your email has existed.")
        else:
            raise forms.ValidationError("Please enter a valid email address.")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if len(password1) < 8:
            raise forms.ValidationError("Your password must have at least 8 characters.")
        elif len(password1) > 16:
            raise forms.ValidationError("Your password is too long.")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password mismatch. Please enter again")

        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean_username(username):
        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError("This email does not exist.")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError("This username does not exist. Please register first.")

        return username


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=32, required=False)
    last_name = forms.CharField(label="Last Name", max_length=32, required=False)
    org = forms.CharField(label="Organization", max_length=128, required=False)
    phone = forms.CharField(label="Phone", max_length=64, required=False)


class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password', max_length=16)
    password1 = forms.CharField(label='New Password', max_length=16)
    password2 = forms.CharField(label='Confirm Password', max_length=16)
