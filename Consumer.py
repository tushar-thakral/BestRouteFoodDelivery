from Location import HasLocation, Location


class Consumer(HasLocation):

    def __init__(self, name: str, location: Location, waiting_time: float):
        super().__init__(name, location, waiting_time=0)
