from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["name"]
    objects=UserManager()
