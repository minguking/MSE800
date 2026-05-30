# Activity 3 – Single Inheritance: Air New Zealand Flight System

Demonstrates single inheritance in Python using an Air New Zealand domestic flight system.

## Class Structure

| Class | Type | Description |
|-------|------|-------------|
| `Flight` | Parent | General flight with shared attributes and methods |
| `DomesticFlight` | Child | Inherits from `Flight`, adds NZ domestic-specific features |

### Inherited (Parent → Child)
- Attributes: `flight_number`, `origin`, `destination`, `departure_time`
- Methods: `book_seat()`

### Overridden in Child
- `get_flight_info()` — extends parent output with `region` and island info

### Child-only
- `is_north_island: bool`
- `is_heading_to_north_island()` — returns which island the flight is heading to

## How to Run

```bash
python air_nz.py
```

### Expected Output

```
=== General Flight (Parent) ===
Flight NZ001: Auckland -> Sydney at 08:00
Seat booked on flight NZ001.

=== Domestic Flight ===
Flight NZ422: Auckland -> Queenstown at 10:30 | Region: South Island | heading to North Island: False
Seat booked on flight NZ422.
Flight NZ422 heading to South Island
```
