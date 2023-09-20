from package.models import (
    Business,
    Hall,
    Catress,
    Package
)


def create_package(hall):
    print("hall--------------->>>>>", hall)
    if hall is not None:
        # hall = Hall.objects.get(id=hall_id)
        package_type = hall.package_preference
        Area = hall.area
        # package_type = Hall.objects.get(id=hall).package_preference
        # Area = Hall.objects.get(id=hall).area
        print("package_type---->>", package_type)
        print("Area ---->>>", Area)
        catress = Catress.objects.get(area=Area)
        print("catress --->", catress)
        package_price = catress.total_price + hall.price_par_wedding
        print(package_price)
        package = Package.objects.create(hall_fk=hall, package_type=package_type, catress_fk=catress, package_price=package_price)
        package.save()

    return package
