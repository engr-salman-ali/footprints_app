from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class TodoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    task = models.CharField(max_length=512, blank=False , null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
