from typing import List

# Constants
MAX_FARE = 3.20
BUS_FARE = 1.80

class Station:
    """
    Single Responsibility Principle (SRP):
    This class is responsible for managing station details, 
    including the name and the zones associated with the station.
    """
    def __init__(self, name: str, zones: List[int]):
        self.name = name
        self.zones = zones

class Trip:
    """
    SRP:
    This class is responsible for managing a trip, including
    calculating the fare based on the start and end stations.

    Open/Closed Principle (OCP):
    This class can be extended for different types of trips or
    fare calculations without modifying the existing code.
    """
    def __init__(self, start_station: Station, end_station: Station = None):
        self.start_station = start_station
        self.end_station = end_station

    def calculate_fare(self) -> float:
        """
        This method calculates the fare based on the zones of the 
        start and end stations. If no end station is provided, it 
        returns the maximum fare.
        """
        if self.end_station is None:
            return MAX_FARE
        
        start_zones = set(self.start_station.zones)
        end_zones = set(self.end_station.zones)

        if 1 in start_zones and 1 in end_zones:
            return 2.50
        elif len(start_zones.intersection(end_zones)) > 0:
            return 2.00
        elif start_zones.union(end_zones) == {2, 3}:
            return 2.25
        elif len(start_zones.union(end_zones)) > 2:
            return 3.20
        else:
            return 3.00

class OysterCard:
    """
    SRP:
    This class is responsible for managing the Oyster card balance, 
    loading money onto the card, and adjusting the balance for trips.

    OCP:
    The OysterCard class can be extended to handle different types of 
    fare calculations or additional card functionalities without 
    modifying the existing code.

    Dependency Inversion Principle (DIP):
    The class uses abstractions like the Trip class to manage different 
    types of trips, rather than depending on concrete implementations.
    """
    def __init__(self, balance: float = 0):
        self.balance = balance

    def load(self, amount: float):
        """
        Load money onto the Oyster card.
        """
        self.balance += amount

    def deduct(self, amount: float):
        """
        Deduct a specified amount from the balance.
        Raises an exception if the balance is insufficient.
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def make_trip(self, trip: Trip):
        """
        Deducts the maximum fare initially, then adjusts the balance 
        after calculating the actual fare for the trip.
        """
        self.deduct(MAX_FARE)
        actual_fare = trip.calculate_fare()
        self.balance += (MAX_FARE - actual_fare)

    def bus_trip(self):
        """
        Deducts a flat fare for bus journeys.
        """
        self.deduct(BUS_FARE)

    def get_balance(self) -> float:
        """
        Returns the current balance on the card.
        """
        return self.balance

# Testing (TDD Approach)
def test_oyster_card_system():
    """
    Test-Driven Development (TDD) Approach:
    This function defines test cases to ensure the Oyster card system 
    meets the specified requirements.

    - Initial Setup: The card is loaded with £30.
    - Test Trips: 
        * Tube from Holborn to Earl's Court.
        * Bus from Earl's Court to Chelsea.
        * Tube from Earl's Court to Hammersmith.
    - Assertion: Verify the final balance matches the expected amount.
    """
    holborn = Station("Holborn", [1])
    earls_court = Station("Earl's Court", [1, 2])
    hammersmith = Station("Hammersmith", [2])
    chelsea = Station("Chelsea", [])  # No zone for bus trips

    card = OysterCard()
    card.load(30.0)

    # Tube Holborn to Earl's Court
    trip1 = Trip(holborn, earls_court)
    card.make_trip(trip1)

    # Bus 328 from Earl's Court to Chelsea
    card.bus_trip()

    # Tube Earl's Court to Hammersmith
    trip2 = Trip(earls_court, hammersmith)
    card.make_trip(trip2)

    # Asserting the final balance
    assert card.get_balance() == 30.0 - (2.50 + BUS_FARE + 2.00), "Balance calculation failed"

    # Printing the final balance for verification
    print(f"Final Balance: £{card.get_balance():.2f}")

if __name__ == "__main__":
    # Test case run
    test_oyster_card_system()
