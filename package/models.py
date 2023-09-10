from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from user.models import *
from package.utilities.choices import BusinessChoice
# class package(models.Model):
#     pass

class Business(models.Model):
    user_fk = models.ForeignKey(User, verbose_name="Vender", on_delete = models.CASCADE, related_name="hall_renter")
    business_name = models.CharField(_('Business Name'),max_length=256)
    # business_type = models.PositiveSmallIntegerField(
    #     _("Business Type"), choices=BusinessChoice.choices,
    #     null=True, blank=True
    # )
    business_type = models.PositiveSmallIntegerField(
        _("Business Type"), choices=BusinessChoice.choices
    )
    # ----------package_preference----------
    # premium = models.BooleanField(_('Premium'), null=True, blank=True)  # 50 lak +
    # economical = models.BooleanField(_('Economical'), null=True, blank=True) # 10 to 50
    # budget = models.BooleanField(_('Budget'), null=True, blank=True) # Under 10

    business_address = models.CharField(_('Business Address'), null=True, blank=True, max_length=200)
    country = models.ForeignKey(
        "user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE
    )
    states = models.ForeignKey(
        "user.State", verbose_name=_("State FK"), on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        "user.District", verbose_name=_("District FK"), on_delete=models.CASCADE
    )
    contect_no = models.CharField(_('Contect Number'), max_length=13)

    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return str(self.business_name)


class Package(models.Model):
    pass
    # business_fk = models.ForeignKey(Business, verbose_name="Business", on_delete=models.CASCADE, related_name="Business" )




# class Hall_Renter(models.Model):
#     user_fk = models.ForeignKey(User, verbose_name="Vender", on_delete = models.CASCADE, null=True, blank=True, related_name="hall_renter")
#     hall_fk = models.ForeignKey(Business, verbose_name="Hall", on_delete = models.CASCADE, null=True, blank=True, related_name="hall")
#     contect_no = models.CharField(_('Contect Number'), max_length=13)

#     def __str__(self):
#         return self.hall_fk


# class Catress(models.Model):
#     user_fk = models.ForeignKey(User, verbose_name="Vender", on_delete = models.CASCADE, null=True, blank=True, related_name="catress")
#     catress_fk = models.ForeignKey(Business, verbose_name="Catress", on_delete = models.CASCADE, null=True, blank=True, related_name="catress")
#     contect_no = models.CharField(_('Contect Number'), max_length=13)

#     def __str__(self):
#         return self.catress_fk

