from abc import ABC, abstractmethod
from copy import deepcopy

import FoodDeliveryAgent
from Consumer import Consumer
from DistanceCalculationStrategy import DistanceCalculationStrategy
from Restaurant import Restaurant


class RouteCalculationStrategy(ABC):

    def __init__(self, speed = 5.56): # Speed in metres/second

        self._speed = speed

    @property
    def speed(self) -> float:
        return self._speed

    @abstractmethod
    def find_best_route(self, restaurant1: Restaurant, consumer1: Consumer, restaurant2: Restaurant, consumer2: Consumer, food_delivery_agent: FoodDeliveryAgent, distance_calculation_strategy: DistanceCalculationStrategy) -> str:
        pass


class TotalMinimumTimeStrategy(RouteCalculationStrategy):

    def __init__(self):

        super().__init__()
        self._consumer_restaurant_mapping = {}
        self._objects_list = []
        self._minimum_time = float('inf')
        self._visited = {}
        self._order_sequence = []

    def find_best_route(self, restaurant1: Restaurant, consumer1: Consumer, restaurant2: Restaurant, consumer2: Consumer, food_delivery_agent: FoodDeliveryAgent, distance_calculation_strategy: DistanceCalculationStrategy) -> str:

        best_route = "Sequence = "
        self._consumer_restaurant_mapping = { consumer1: restaurant1, consumer2: restaurant2 }
        self._objects_list = [ consumer1, consumer2, restaurant1, restaurant2 ]
        self._order_sequence = [ food_delivery_agent ]

        for obj in self._objects_list:
            self._visited[obj] = False

        def best_route_sequence(index, current_sequence, time) -> None:
            """Uses Backtracking algorithm to find out the best route."""

            if index == 4:
                if time < self._minimum_time:
                    self._minimum_time = time
                    self._order_sequence = deepcopy(current_sequence)
                return

            for objec in self._objects_list:

                if objec in self._consumer_restaurant_mapping and self._visited[self._consumer_restaurant_mapping[objec]] and not self._visited[objec]:
                    time_to_add = distance_calculation_strategy.calculate_distance(current_sequence[-1].location, objec.location) / self._speed
                    time += time_to_add
                    self._visited[objec] = True
                    current_sequence.append(objec)
                    best_route_sequence(index+1, current_sequence, time)
                    self._visited[objec] = False
                    time -= time_to_add
                    current_sequence.pop()

                elif objec not in self._consumer_restaurant_mapping and not self._visited[objec]:
                    time_to_add = distance_calculation_strategy.calculate_distance(current_sequence[-1].location, objec.location) / self._speed
                    if objec.waiting_time > time:
                        time_to_add += (objec.waiting_time - time)
                    time += time_to_add
                    self._visited[objec] = True
                    current_sequence.append(objec)
                    best_route_sequence(index + 1, current_sequence, time)
                    self._visited[objec] = False
                    time -= time_to_add
                    current_sequence.pop()

        best_route_sequence(0,[ food_delivery_agent ], 0)

        for obj in self._order_sequence:
            best_route += obj.name + " "

        best_route.strip()
        return best_route


class RouteCalculator:

    def __init__(self, restaurant1: Restaurant, consumer1: Consumer, restaurant2: Restaurant, consumer2: Consumer, food_delivery_agent: FoodDeliveryAgent, route_calculation_strategy: RouteCalculationStrategy, distance_calculation_strategy: DistanceCalculationStrategy):
        self._restaurant1 = restaurant1
        self._consumer1 = consumer1
        self._restaurant2= restaurant2
        self._consumer2 = consumer2
        self._food_delivery_agent= food_delivery_agent
        self._route_calculation_strategy = route_calculation_strategy
        self._distance_calculation_strategy = distance_calculation_strategy

    @property
    def restaurant1(self) -> Restaurant:
        return self._restaurant1

    @property
    def restaurant2(self) -> Restaurant:
        return self._restaurant2

    @property
    def consumer1(self) -> Consumer:
        return self._consumer1

    @property
    def consumer2(self) -> Consumer:
        return self._consumer2

    @property
    def food_delivery_agent(self) -> FoodDeliveryAgent:
        return self._food_delivery_agent

    def find_best_delivery_route(self):
        best_route = self._route_calculation_strategy.find_best_route(self._restaurant1, self._consumer1, self._restaurant2, self._consumer2, self._food_delivery_agent, self._distance_calculation_strategy)
        print(best_route)

