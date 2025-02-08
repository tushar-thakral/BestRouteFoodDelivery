from abc import ABC, abstractmethod

from Location import Location


class DistanceCalculationStrategy(ABC):

    @abstractmethod
    def calculate_distance(self, location1: Location, location2: Location) -> float:
        pass


class HaversineDistanceStrategy(DistanceCalculationStrategy):

    def calculate_distance(self, location1: Location, location2: Location) -> float:

        import math

        lon1, lat1 = location1.longitude, location1.latitude
        lon2, lat2 = location2.longitude, location2.latitude

        R = 6371000  # radius of Earth in meters
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)

        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        meters = R * c  # output distance in meters
        meters = round(meters, 3)

        return meters