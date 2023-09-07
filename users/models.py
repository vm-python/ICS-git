from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpeg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} profile'

    def get_absolute_url(self):
        return reverse("profile")

