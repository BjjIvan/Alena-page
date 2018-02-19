from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.full_name


class UserprofileInfo(models.Model):

    user = models.OneToOneField(User)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics")

    def __str__(self):
        return self.user.username

class Lecture(models.Model):
   title = models.CharField(max_length=150)
   date_start = models.DateField(timezone.now(), blank=True, null=True)
   date_end = models.DateField(timezone.now(), blank=True, null=True)




   def __str__(self):
       return self.title
