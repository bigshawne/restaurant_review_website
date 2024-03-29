from allauth.account.models import EmailAddress
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # One to one relationship with user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # The organization is for determining if the user is owner of restaurant
    org = models.CharField(
        'Organization', max_length=128, blank=True
    )

    # allow user model to store phone number of users
    phone = models.CharField(
        'Phone', max_length=20, blank=True
    )

    # Record the mod date
    mod_date = models.DateTimeField('Last modified', auto_now=True)


    class Meta:
        verbose_name = 'User Profile'


    def __str__(self):
        return self.user

    def account_verifited(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
