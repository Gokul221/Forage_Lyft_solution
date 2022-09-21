from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_grades):
        self.tire_grades = tire_grades

    def needs_service(self):
        tire_wear_level = 0.0

        for grade in self.tire_grades:
            tire_wear_level += grade

        if tire_wear_level >= 3.0:
            return True
        else:
            return False
