def car_info(manufacturer, model, **kwargs):
    """Ek dictionary return karne wala function jo car ki details store karega"""
    car_details = {
        "Manufacturer": manufacturer,
        "Model": model
    }
    car_details.update(kwargs)  # Extra information add karna
    return car_details

# Function ko call karna aur car details print karna
car1 = car_info("Toyota", "Corolla", color="White", sunroof=True)
car2 = car_info("Honda", "Civic", color="Black", engine="V6")

# Output print karna
print(car1)
print(car2)
