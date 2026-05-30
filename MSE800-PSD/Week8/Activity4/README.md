# Activity 4 – Hybrid Inheritance: Air New Zealand Flight Management System

Demonstrates **hybrid inheritance** (Hierarchical + Multiple) using an Air New Zealand flight management system.

## Inheritance Structure

```
             Flight                  ← Base class
            /      \
 DomesticFlight  InternationalFlight  ← Hierarchical inheritance
            \      /
          CharterFlight                ← Multiple inheritance → Hybrid
```

## Class Overview

| Class | Inherits From | Type |
|-------|--------------|------|
| `Flight` | — | Base class |
| `DomesticFlight` | `Flight` | Hierarchical |
| `InternationalFlight` | `Flight` | Hierarchical |
| `CharterFlight` | `DomesticFlight`, `InternationalFlight` | Multiple (Hybrid) |

## Methods per Class

### `Flight` (Base)
| Method | Description |
|--------|-------------|
| `get_flight_info()` | Returns basic flight details |
| `book_seat()` | Books a seat on the flight |
| `cancel_seat()` | Cancels an existing booking |

### `DomesticFlight` (Child)
| Method | Description |
|--------|-------------|
| `get_flight_info()` | Overrides parent — adds region info |
| `is_heading_to_north_island()` | Returns which NZ island the flight heads to |
| `get_domestic_details()` | Returns full domestic flight summary |

### `InternationalFlight` (Child)
| Method | Description |
|--------|-------------|
| `get_flight_info()` | Overrides parent — adds destination country |
| `check_travel_documents()` | Lists required passport/visa documents |
| `get_international_details()` | Returns full international flight summary |

### `CharterFlight` (Grandchild — Hybrid)
| Method | Description |
|--------|-------------|
| `get_flight_info()` | Combines base, region, country, and loyalty points |
| `earn_loyalty_points(miles)` | Calculates and adds Airpoints earned |
| `get_flight_summary()` | Full summary using inherited methods from both parents |

## How to Run

```bash
python air_nz.py
```

### Expected Output

```
=== Base Flight (Parent) ===
[NZ001] Auckland -> Sydney | Departs: 08:00
Seat booked on flight NZ001.
Booking cancelled on flight NZ001.

=== Domestic Flight (Child - Hierarchical) ===
[NZ422] Auckland -> Queenstown | Departs: 10:30 | Region: South Island
Flight NZ422 is heading to South Island.
Domestic Flight NZ422: Auckland -> Queenstown | Region: South Island

=== International Flight (Child - Hierarchical) ===
[NZ105] Auckland -> Tokyo | Departs: 23:00 | Destination Country: Japan
Required documents for Japan: Passport.
International Flight NZ105: Auckland -> Tokyo | Country: Japan | Passport: True | Visa: False

=== Air NZ Flight (Child - Multiple/Hybrid) ===
[NZ290] Christchurch -> Melbourne | Departs: 14:00 | Region: South Island | Country: Australia | Points: 500
Earned 1600 Airpoints on flight NZ290. Total: 2100
=== Air NZ Flight Summary ===
  [NZ290] Christchurch -> Melbourne | Departs: 14:00 | Region: South Island | Country: Australia | Points: 2100
  Required documents for Australia: Passport.
  Flight NZ290 is heading to South Island.
```
