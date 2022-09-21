from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_grades):
        self.tire_grades = tire_grades

    def needs_service(self):
        for grade in self.tire_grades:
            if grade >= 0.9:
                return True
        return False
