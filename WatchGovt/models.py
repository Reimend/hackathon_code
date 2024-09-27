from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

# Update settings.py
AUTH_USER_MODEL = 'projects.CustomUser'

# Create your models here.



class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    timeline = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
