from package.models import (
    Business,
    Hall,
    Catress,
    Package
)


def create_package(hall):
    if hall is not None:
        package_type = Hall.objects.get(id=hall).package_preference
        Area = Hall.objects.get(id=hall).area
        print("package_type---->>", package_type)
        print("Area ---->>>", Area)
        catress = Catress.objects.get(area=Area).id
        print("catress --->", catress)
        package = Package.objects.create(hall_fk=hall, package_type=package_type, catress_fk=catress)

    return package
