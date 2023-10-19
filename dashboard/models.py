from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=99)
    date_posted = models.DateTimeField(default=timezone.now)
    fed_tax_id = models.CharField(max_length=9)
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_state = models.CharField(max_length=2)
    address = models.TextField()
    zip_code = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.name} owned by {self.officer.username}'
    
    def get_absolute_url(self):
        return reverse("company-detail", kwargs={'pk': self.pk})


class Project(models.Model):
    name = models.CharField(max_length=99)
    date_posted = models.DateTimeField(default=timezone.now)
    parent_company=models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("project-detail", kwargs={'pk': self.pk})



class Task(models.Model):
    name = models.CharField(max_length=99)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("task-detail", kwargs={'pk': self.pk})
