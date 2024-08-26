from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
# Create your models here.


class UserManager(BaseUserManager):
    """
    Customizing the User model to create it only using the email and passsword.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save the user using the email and password fields.
        """
        if not email:
            raise ValueError('You must provide an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('The superuser must have "is_staff= True"'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('The superuser must have "is_superuser=True"'))
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    """
    Customizing the User Model
    """
    email = models.EmailField(unique= True, null= False)
    is_staff = models.BooleanField(
        gettext_lazy('staff'),
        default= False,
        help_text= gettext_lazy('Designates whether the user can login or not')
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default= True,
        help_text= gettext_lazy('Unselect instead of deleting the account.')
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
