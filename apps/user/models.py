from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.user.customs.managers import UserManager
from apps.user.utilities.choices import UserRoleChoices



class User(AbstractBaseUser):
    """
    User model
    """

    email = models.EmailField(_("Email"), max_length=255, unique=True)
    full_name = models.CharField(_("Name"), max_length=50)
    mobile = PhoneNumberField(_("Mobile Number"), null=True, blank=True, unique=True)
    password = models.CharField(_("Password"), max_length=200)
    user_image = models.ImageField(
        _("User Image"),
        null=True,
        blank=True,
        upload_to="media/user",
        default="media/user/user_318-159711.png",
    )
    user_role = models.PositiveSmallIntegerField(
        _("User Role"), choices=UserRoleChoices.choices, default=3
    )
    is_staff = models.BooleanField(_("Staff Status"), default=False)
    is_superuser = models.BooleanField(_("Superuser Status"), default=False)
    is_active = models.BooleanField(_("Superuser Status"), default=True)

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    last_login = models.DateTimeField(
        _("Last Login"), auto_now=False, auto_now_add=False, blank=True, null=True
    )
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "password", "user_role"]


    mobile_verify = models.BooleanField(_("Mobile Number Verify"), default=False)
    email_verify = models.BooleanField(_("Email Verify"), default=False)
    # mobile_otp = models.IntegerField(_("Mobile OTP"), default=0)
    # is_pass_changed = models.BooleanField(_("Password Changed"), default=False)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return str(self.email)