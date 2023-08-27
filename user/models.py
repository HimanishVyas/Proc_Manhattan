from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from user.customs.managers import UserManager
from user.utilities.choices import UserRoleChoices



class User(AbstractBaseUser):
    """
    User model
    """

    email = models.EmailField(_("Email"), max_length=255, unique=True)
    name = models.CharField(_("Name"), max_length=50)
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
    # fcm_token = models.TextField(_("Fcm Token"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password", "mobile", "user_role"]
    mobile_verify = models.BooleanField(_("Mobile Number Verify"), default=False)
    email_verify = models.BooleanField(_("Email Verify"), default=False)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return str(self.email)


class Address(models.Model):
    user_fk = models.ForeignKey(User, verbose_name=_("User FK"), on_delete=models.SET_NULL, null=True, blank=True, related_name="User_fk")
    address = models.TextField(_("Address"))
    country = models.ForeignKey(
        "user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE
    )
    states = models.ForeignKey(
        "user.State", verbose_name=_("State FK"), on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        "user.District", verbose_name=_("District FK"), on_delete=models.CASCADE
    )
    city = models.CharField(_("City"), max_length=50)
    pincode = models.CharField(_("PinCode"), max_length=50)
    is_active = models.BooleanField(_("Is Active"), default=True)
    def __str__(self):
        return str(self.address)


class Country(models.Model):
    country = models.CharField(max_length=256)

    def __str__(self):
        return str(self.country)


class State(models.Model):
    country_fk = models.ForeignKey(
        Country,
        verbose_name=_("country FK"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="state",
    )
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.state)


class District(models.Model):
    state_fk = models.ForeignKey(
        State,
        verbose_name=_("State FK"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="country",
    )
    district = models.CharField(max_length=100)

    def __str__(self):
        return str(self.district)