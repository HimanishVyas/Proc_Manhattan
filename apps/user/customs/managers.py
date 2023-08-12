import datetime

from django.contrib.auth.models import BaseUserManager
from django.db import models

# from apps.user.customs.querysets import SoftDeletionQuerySet


# class SoftDeletionManager(models.Manager):
#     def __init__(self, *args, **kwargs):
#         self.alive_only = kwargs.pop("alive_only", True)
#         super(SoftDeletionManager, self).__init__(*args, **kwargs)

#     def get_queryset(self):
#         if self.alive_only:
#             return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
#         return SoftDeletionQuerySet(self.model)

#     def hard_delete(self):
#         return self.get_queryset().hard_delete()


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        user_role,
        password=None,
        full_name=None,
        user_image=None,
        *args,
        **kwargs,
    ):
        if not email:
            raise ValueError("User must have an email address")
        if super().get_queryset().filter(email=self.normalize_email(email)):
            raise ValueError("User with this email address already exists")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password,
            user_role=user_role,
            user_image=user_image,
            last_login=datetime.datetime.now(),
            *args,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        password=None,
        full_name=None,
        user_role=1,
    ):
        user = self.create_user(
            email,
            password=password,
            user_role=1,
            full_name=full_name,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create(self, **kwargs):
        return self.model.objects.create_user(**kwargs)
