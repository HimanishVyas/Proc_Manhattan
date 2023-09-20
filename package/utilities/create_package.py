from package.models import (
    Business,
    Hall,
    Catress,
    Package
)


def create_package(hall):
    if hall is not None:
        package_type = hall.package_preference
        Area = hall.area
        catress = Catress.objects.get(area=Area)
        package_price = catress.total_price + hall.price_par_wedding
        package = Package.objects.create(hall_fk=hall, package_type=package_type, catress_fk=catress, package_price=package_price)
        package.save()

    return package
