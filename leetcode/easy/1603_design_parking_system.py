"""
https://leetcode.com/problems/design-parking-system/
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        space_available = False
        if self.spaces[carType - 1]:
            space_available = True
            self.spaces[carType - 1] -= 1
        return space_available


parkingSystem = ParkingSystem(1, 1, 0)
assert parkingSystem.addCar(1) is True  # return true because there is 1 available slot for a big car
assert parkingSystem.addCar(2) is True  # return true because there is 1 available slot for a medium car
assert parkingSystem.addCar(3) is False  # return false because there is no available slot for a small car
assert parkingSystem.addCar(1) is False  # there is no available slot for a big car. It is already occupied.
