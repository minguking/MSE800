# Parent class: represents a general flight
class Flight:
    def __init__(self, flight_number, origin, destination, departure_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time

    # Shared method
    def get_flight_info(self):
        return (f"Flight {self.flight_number}: {self.origin} -> {self.destination} "
                f"at {self.departure_time}")

    def book_seat(self):
        return f"Seat booked on flight {self.flight_number}."


# Child class: represents a domestic flight, inherits from Flight
class DomesticFlight(Flight):
    def __init__(self, flight_number, origin, destination, departure_time,
                 region, is_north_island):
        
        super().__init__(flight_number, origin, destination, departure_time)

        # Domestic-specific attributes
        self.region = region
        self.is_north_island = is_north_island

    def get_flight_info(self):
        base_info = super().get_flight_info()
        return f"{base_info} | Region: {self.region} | heading to North Island: {self.is_north_island}"
    
    def is_heading_to_north_island(self):
        return f"Flight {self.flight_number} heading to {('North Island') if self.is_north_island else ('South Island')}"


## -- Demo --
if __name__ == "__main__":

    # Parent instance
    general = Flight("NZ001", "Auckland", "Sydney", "08:00")

    # Child instance
    domestic = DomesticFlight("NZ422", "Auckland", "Queenstown", "10:30",
                              region="South Island", is_north_island=False)

    print("=== General Flight (Parent) ===")
    print(general.get_flight_info())
    print(general.book_seat())

    print("\n=== Domestic Flight ===")
    print(domestic.get_flight_info())
    print(domestic.book_seat())
    print(domestic.is_heading_to_north_island())
