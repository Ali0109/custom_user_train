from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_softdelete.models import SoftDeleteModel, SoftDeleteQuerySet


class CustomAccountManager(BaseUserManager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(is_deleted=False)

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, password, **other_fields)

    def create_staff(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Staff must be assigned to is_staff=True')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("You must provide an phone number")

        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(SoftDeleteModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(null=True, blank=True, max_length=255)
    gender = models.CharField(null=True, blank=True, max_length=255)
    birthday = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['id']
