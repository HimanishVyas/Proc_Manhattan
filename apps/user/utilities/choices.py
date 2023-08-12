from django.db import models
from django.utils.translation import gettext_lazy as _




class UserRoleChoices(models.IntegerChoices):
    CUSTOMER = 1, _("Customer")
    VENDOR = 2, _("Vendor")