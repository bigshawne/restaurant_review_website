from django import forms
from .models import UserProfile


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=32, required=False)
    last_name = forms.CharField(label="Last Name", max_length=32, required=False)
    org = forms.CharField(label="Organization", max_length=128, required=False)
    phone = forms.CharField(label="Phone", max_length=64, required=False)


class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = UserProfile();
        user_profile.user = user
        user.save()
        user_profile.save()