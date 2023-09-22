from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from user.models import *
from package.utilities.choices import BusinessChoice, PackageTypeChoice


# class package(models.Model):
#     pass

class Business(models.Model):
    user_fk = models.ForeignKey(User, verbose_name="Vender", on_delete=models.CASCADE, related_name="hall_renter")
    business_name = models.CharField(_('Business Name'), max_length=256, unique=True)
    business_type = models.PositiveSmallIntegerField(_("Business Type"), choices=BusinessChoice.choices)
    business_address = models.CharField(_('Business Address'), null=True, blank=True, max_length=200)
    country = models.ForeignKey("user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE)
    states = models.ForeignKey("user.State", verbose_name=_("State FK"), on_delete=models.CASCADE)
    district = models.ForeignKey("user.District", verbose_name=_("District FK"), on_delete=models.CASCADE)
    contect_no = models.CharField(_('Contect Number'), max_length=13)
    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return str(self.business_name)


# class Frenchies(models.Model):
#
#     business_fk = models.ForeignKey(Business, verbose_name="Business", on_delete = models.CASCADE, related_name="business")
#     frenchies_name = models.CharField(verbose_name="Frenchies Name", max_length=200, null=True, blank=True)
#     frenchies_address = models.CharField(_('Frenchies Address'), null=True, blank=True, max_length=200)
#     price_par_wedding = models.FloatField(verbose_name="Price Par Wedding", null=True, blank=True)
#     area = models.CharField(_("Area"), null=True, blank=True, max_length=100)
#     country = models.ForeignKey("user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE)
#     states = models.ForeignKey("user.State", verbose_name=_("State FK"), on_delete=models.CASCADE)
#     district = models.ForeignKey("user.District", verbose_name=_("District FK"), on_delete=models.CASCADE)
#     contect_no = models.CharField(_('Contect Number'), max_length=13, unique=True)
#     is_contect_no_verified = models.BooleanField(_("Is Contect No Active"), default=True)
#     is_active = models.BooleanField(_("Is Active"), default=True)
#
#     def __str__(self):
#         return self.frenchies_name

class Hall(models.Model):
    business_fk = models.ForeignKey(Business, verbose_name="Business", on_delete=models.CASCADE)
    hall_name = models.CharField(verbose_name="Hall Name", max_length=200)
    capacity = models.IntegerField(verbose_name="Hall capacity")
    rooms = models.IntegerField(verbose_name="Room Count")
    address = models.CharField(_('Hall Address'), max_length=200)
    price_par_wedding = models.FloatField(verbose_name="Price Par Wedding")
    package_preference = models.PositiveSmallIntegerField(_("Package Preference"), choices=PackageTypeChoice.choices)
    area = models.CharField(_("Area"), max_length=100)
    country = models.ForeignKey("user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE)
    states = models.ForeignKey("user.State", verbose_name=_("State FK"), on_delete=models.CASCADE)
    district = models.ForeignKey("user.District", verbose_name=_("District FK"), on_delete=models.CASCADE)
    contect_no = models.CharField(_('Contect Number'), max_length=13, unique=True)
    is_contect_no_verified = models.BooleanField(_("Is Contect No Active"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return self.hall_name


class Catress(models.Model):
    business_fk = models.ForeignKey(Business, verbose_name="Business", on_delete=models.CASCADE)
    catress_name = models.CharField(verbose_name="Catress Name", max_length=200)
    capacity = models.IntegerField(verbose_name="People capacity")
    address = models.CharField(_('Catress Address'), max_length=200)
    price_par_plate = models.FloatField(verbose_name="Price Par Plate")
    # plate_count = models.IntegerField(verbose_name="Plate Count")
    total_price = models.IntegerField(verbose_name="Price", null=True,
                                      blank=True)  # total_price = plate_count * price_par_plate
    package_preference = models.PositiveSmallIntegerField(_("Package Preference"), choices=PackageTypeChoice.choices)
    area = models.CharField(_("Area"), max_length=100)
    country = models.ForeignKey("user.Country", verbose_name=_("Country FK"), on_delete=models.CASCADE)
    states = models.ForeignKey("user.State", verbose_name=_("State FK"), on_delete=models.CASCADE)
    district = models.ForeignKey("user.District", verbose_name=_("District FK"), on_delete=models.CASCADE)
    contect_no = models.CharField(_('Contect Number'), max_length=13, unique=True)
    is_contect_no_verified = models.BooleanField(_("Is Contect No Active"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)

    def __str__(self):
        return self.catress_name


class Package(models.Model):
    hall_fk = models.ForeignKey(Hall, verbose_name="Hall", on_delete=models.CASCADE, related_name="hall_package")
    catress_fk = models.ForeignKey(Catress, verbose_name="Catress", on_delete=models.CASCADE, related_name="Catress")
    package_price = models.FloatField(verbose_name="Package Price", null=True, blank=True)  # Sum of all venders price
    package_type = models.PositiveSmallIntegerField(_("Package Type"),
                                                    choices=PackageTypeChoice.choices)  # as par price of package
    is_active = models.BooleanField(_("Is Active"), default=True)
    # vender = models.ManyToManyField(Frenchies, verbose_name=_("Frenchies"))
    # package_type = models.PositiveSmallIntegerField(_("Package Type"), choices=PackageTypeChoice.choices)
    # package_price = models.FloatField(verbose_name="Package Price", null=True, blank=True)
    # is_active = models.BooleanField(_("Is Active"), default=True)
