from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear_sensor_data):
        self.tire_wear_sensor_data = tire_wear_sensor_data

    def needs_service(self):
        return sum(self.tire_wear_sensor_data) >= 3.0
