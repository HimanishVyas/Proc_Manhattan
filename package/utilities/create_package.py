from package.models import (
    Business,
    Hall,
    Catress,
    Package
)
from django.db.models import F, Max


def create_package(hall):
    if hall is not None:

        high_hall = Hall.objects.aggregate(max_price=Max('price_par_wedding'))['max_price']
        print("high_hall ===========>>", high_hall)
        # packages_with_highest_price = Package.objects.filter(hall_fk__price_par_wedding=F('hall_fk__max_price'))
        # print("packages_with_highest_price =========>>>>", packages_with_highest_price)
        if hall.price_par_wedding < high_hall.price_par_wedding:
            Area = high_hall.area
            catress = Catress.objects.get(area=Area)
            package_price = catress.total_price + high_hall.price_par_wedding
            Package.objects.update(hall_fk=hall, catress_fk=catress, package_price=package_price)
        else:
            package_type = hall.package_preference
            Area = hall.area
            catress = Catress.objects.get(area=Area)
            package_price = catress.total_price + hall.price_par_wedding
            package = Package.objects.create(hall_fk=hall, package_type=package_type, catress_fk=catress,
                                             package_price=package_price)
            package.save()

    # return package
