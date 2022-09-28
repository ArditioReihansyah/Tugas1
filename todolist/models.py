from datetime import datetime
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())
    title = models.TextField()
    desc = models.TextField()
    is_finished = models.BooleanField(default=False)