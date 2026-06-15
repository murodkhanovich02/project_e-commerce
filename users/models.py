from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices


# Create your models here.
class UserRoleEnum(TextChoices):
    ADMIN = 'ADMIN', 'admin'
    USER = 'USER', 'user'


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', default='profile.png')
    role = models.CharField(max_length=10, choices=UserRoleEnum.choices, default=UserRoleEnum.USER)

    def __str__(self):
        return f"{self.username} - {self.role}"
