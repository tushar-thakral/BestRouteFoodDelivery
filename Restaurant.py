from Location import HasLocation, Location


class Restaurant(HasLocation):

    def __init__(self, name: str, location: Location, time_for_food_prep: float):
        super().__init__(name, location, time_for_food_prep)