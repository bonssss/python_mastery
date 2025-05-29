from car import car

def vehicle():
    Car = car("Toyota", "Corolla", 2020)
    info = Car.display_info
    return info()  # Output: 2020 Toyota Corolla    