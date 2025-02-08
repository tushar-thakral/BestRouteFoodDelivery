from Consumer import Consumer
from DistanceCalculationStrategy import HaversineDistanceStrategy
from FoodDeliveryAgent import FoodDeliveryAgent
from Location import Location
from Restaurant import Restaurant
from RouteCalculator import RouteCalculator, TotalMinimumTimeStrategy


class RouteCalculatorExecution:

    @staticmethod
    def run():

        # Delivery Agent Creation
        delivery_agent_location = Location(longitude=77.647, latitude=12.908) # HSR Layout
        delivery_agent = FoodDeliveryAgent(name="Aman", location=delivery_agent_location, waiting_time=0)

        # Restaurant1 Creation
        restaurant1_location = Location(longitude=77.758, latitude=12.994)  # Whitefield
        restaurant1 = Restaurant(name="R1", location=restaurant1_location, time_for_food_prep=100)

        # Restaurant2 Creation
        restaurant2_location = Location(longitude=77.661, latitude=12.903) # Haralur
        restaurant2 = Restaurant(name="R2", location=restaurant2_location, time_for_food_prep=500)

        # Consumer1 Creation
        consumer1_location = Location(longitude=77.697, latitude=12.959)  # Marathahalli
        consumer1 = Consumer(name="C1", location=consumer1_location, waiting_time=0)

        # Consumer2 Creation
        consumer2_location = Location(longitude=77.625, latitude=12.931)  # Koramangala
        consumer2 = Consumer(name="C2", location=consumer2_location, waiting_time=0)

        # Route Calculation Strategy Creation
        route_calculation_strategy = TotalMinimumTimeStrategy()

        # Distance Calculation Strategy Creation
        distance_calculation_strategy = HaversineDistanceStrategy()

        # Best Route Calculation
        route_calculator = RouteCalculator(restaurant1=restaurant1, consumer1=consumer1, restaurant2=restaurant2, consumer2=consumer2, food_delivery_agent=delivery_agent, route_calculation_strategy=route_calculation_strategy, distance_calculation_strategy=distance_calculation_strategy)
        route_calculator.find_best_delivery_route()

if __name__ == "__main__":
    RouteCalculatorExecution.run()