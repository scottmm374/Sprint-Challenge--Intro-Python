# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]


class Vehicle:  # Base class Vehicle
    def __init__(self):
        pass


class GroundVehicle(Vehicle):  # Parent to Car and Motorcycle, Child to Vehicle
    def __init__(self):
        pass


class Car(GroundVehicle):
    def __init__(self):
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass


class FlightVehicle(Vehicle):  # Child of Vehicle, Parent to Airplane and Starship
    def __init__(self):
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        pass


class Starship(FlightVehicle):
    def __init__(self):
        pass
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
