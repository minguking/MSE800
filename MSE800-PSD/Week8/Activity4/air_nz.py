# Air New Zealand - Hybrid Inheritance Example
# Hybrid = Hierarchical + Multiple Inheritance
#
# Flight (base)
#   ├── DomesticFlight(Flight)       ─┐
#   └── InternationalFlight(Flight)  ─┴── CharterFlight(DomesticFlight, InternationalFlight)


# ── Base class ───────────────────────────────────────────────────────────────

class Flight:
    """Base class representing a general flight."""

    def __init__(self, flight_number, origin, destination, departure_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.is_booked = False

    def get_flight_info(self):
        return (f"[{self.flight_number}] {self.origin} -> {self.destination} "
                f"| Departs: {self.departure_time}")

    def book_seat(self):
        self.is_booked = True
        return f"Seat booked on flight {self.flight_number}."

    def cancel_seat(self):
        if self.is_booked:
            self.is_booked = False
            return f"Booking cancelled on flight {self.flight_number}."
        return f"No active booking on flight {self.flight_number}."


# ── Hierarchical: both inherit from Flight ───────────────────────────────────

class DomesticFlight(Flight):
    """Domestic flight within New Zealand."""

    def __init__(self, flight_number, origin, destination, departure_time,
                 region, is_north_island):
        super().__init__(flight_number, origin, destination, departure_time)
        self.region = region
        self.is_north_island = is_north_island  # True = North Island, False = South Island

    def get_flight_info(self):
        base = super().get_flight_info()
        return f"{base} | Region: {self.region}"

    def is_heading_to_north_island(self):
        island = "North Island" if self.is_north_island else "South Island"
        return f"Flight {self.flight_number} is heading to {island}."

    def get_domestic_details(self):
        return (f"Domestic Flight {self.flight_number}: "
                f"{self.origin} -> {self.destination} | Region: {self.region}")


class InternationalFlight(Flight):
    """International flight departing from New Zealand."""

    def __init__(self, flight_number, origin, destination, departure_time,
                 country, passport_required, visa_required):
        super().__init__(flight_number, origin, destination, departure_time)
        self.country = country
        self.passport_required = passport_required
        self.visa_required = visa_required

    def get_flight_info(self):
        base = super().get_flight_info()
        return f"{base} | Destination Country: {self.country}"

    def check_travel_documents(self):
        docs = []
        if self.passport_required:
            docs.append("Passport")
        if self.visa_required:
            docs.append("Visa")
        return f"Required documents for {self.country}: {', '.join(docs) if docs else 'None'}."

    def get_international_details(self):
        return (f"International Flight {self.flight_number}: "
                f"{self.origin} -> {self.destination} | Country: {self.country} "
                f"| Passport: {self.passport_required} | Visa: {self.visa_required}")


# ── Multiple: CharterFlight inherits from both ─────────────────────────────────

class CharterFlight(DomesticFlight, InternationalFlight):
    """
    Air NZ flagship flight class.
    Demonstrates hybrid inheritance by combining DomesticFlight and InternationalFlight.
    """

    def __init__(self, flight_number, origin, destination, departure_time,
                 region, is_north_island, country, passport_required, visa_required,
                 loyalty_points):
        # Call the top-level base to avoid MRO conflict between parent __init__ chains
        Flight.__init__(self, flight_number, origin, destination, departure_time)

        # Set DomesticFlight attributes directly
        self.region = region
        self.is_north_island = is_north_island

        # Set InternationalFlight attributes directly
        self.country = country
        self.passport_required = passport_required
        self.visa_required = visa_required

        self.loyalty_points = loyalty_points

    def get_flight_info(self):
        # Build from base to avoid duplicate fields from both parent chains
        base = Flight.get_flight_info(self)
        return (f"{base} | Region: {self.region} "
                f"| Country: {self.country} | Points: {self.loyalty_points}")

    def earn_loyalty_points(self, miles):
        earned = miles * 2           # Air NZ earns double points
        self.loyalty_points += earned
        return (f"Earned {earned} Airpoints on flight {self.flight_number}. "
                f"Total: {self.loyalty_points}")

    def get_flight_summary(self):
        return (f"=== Air NZ Flight Summary ===\n"
                f"  {self.get_flight_info()}\n"
                f"  {self.check_travel_documents()}\n"   # inherited from InternationalFlight
                f"  {self.is_heading_to_north_island()}")  # inherited from DomesticFlight


# ── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    print("=== Base Flight (Parent) ===")
    general = Flight("NZ001", "Auckland", "Sydney", "08:00")
    print(general.get_flight_info())
    print(general.book_seat())
    print(general.cancel_seat())

    print("\n=== Domestic Flight (Child - Hierarchical) ===")
    domestic = DomesticFlight("NZ422", "Auckland", "Queenstown", "10:30",
                              region="South Island", is_north_island=False)
    print(domestic.get_flight_info())
    print(domestic.is_heading_to_north_island())
    print(domestic.get_domestic_details())

    print("\n=== International Flight (Child - Hierarchical) ===")
    intl = InternationalFlight("NZ105", "Auckland", "Tokyo", "23:00",
                               country="Japan", passport_required=True, visa_required=False)
    print(intl.get_flight_info())
    print(intl.check_travel_documents())
    print(intl.get_international_details())

    print("\n=== Air NZ Flight (Child - Multiple/Hybrid) ===")
    airnz = CharterFlight(
        flight_number="NZ290",
        origin="Christchurch", destination="Melbourne",
        departure_time="14:00",
        region="South Island", is_north_island=False,
        country="Australia", passport_required=True, visa_required=False,
        loyalty_points=500
    )
    print(airnz.get_flight_info())
    print(airnz.earn_loyalty_points(miles=800))
    print(airnz.get_flight_summary())
