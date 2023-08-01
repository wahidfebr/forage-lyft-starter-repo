from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_sensor_data):
        self.tire_wear_sensor_data = tire_wear_sensor_data

    def needs_service(self):
        return any(map(lambda current_tire: current_tire >= 0.9, self.tire_wear_sensor_data))
