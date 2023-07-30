from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 99)
    date_posted = models.DateTimeField(default=timezone.now)
    fed_tax_id = models.CharField(max_length = 9)
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_state = models.CharField(max_length = 2)
    address = models.TextField()
    zip_code = models.CharField(max_length = 9)

    def __str__(self):
        return f'{self.name} owned by {self.officer.username}'
