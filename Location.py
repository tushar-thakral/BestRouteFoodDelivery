from abc import ABC

class Location:

    def __init__(self, longitude: float, latitude: float):
        self._longitude = longitude
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude


class HasLocation(ABC):

    def __init__(self, name: str, location: Location, waiting_time: float):
        self._name = name
        self._location = location
        self._waiting_time = waiting_time

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def waiting_time(self) -> float:
        return self._waiting_time