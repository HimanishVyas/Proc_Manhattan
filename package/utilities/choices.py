from django.db import models
from django.utils.translation import gettext_lazy as _




class BusinessChoice(models.IntegerChoices):
    HallRenter = 1, _("Hall Renter")
    Catress = 2, _("Catress")