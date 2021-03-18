from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager ,PermissionsMixin


class UserManager(BaseUserManager):
    def crete_user(self,email, password=None, **extra_fields):
        """create and saves a newe user """
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    """custom user model that support email instead of username"""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

