from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User_staff(AbstractUser):
    fullname = models.CharField(max_length=100)
