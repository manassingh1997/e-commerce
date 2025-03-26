from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role='boyer'):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username, email, password=None):
        user = self.create_user(username, email, password, role='seller')
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.role}"