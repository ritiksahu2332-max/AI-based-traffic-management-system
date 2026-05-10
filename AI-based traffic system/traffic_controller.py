from config import *

class TrafficController:
    def __init__(self):
        self.green_time = GREEN_MIN

    def calculate_green_time(self, vehicle_count):
        if vehicle_count < 5:
            self.green_time = 5

        elif vehicle_count < 10:
            self.green_time = 10

        elif vehicle_count < 20:
            self.green_time = 20

        else:
            self.green_time = GREEN_MAX

        return self.green_time