# Here’s the structured response for the Parking Lot system:


# Class Structure for Parking Lot System

from enum import Enum
from typing import List, Dict, Optional


# Enums
class CarSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class SpaceStatus(Enum):
    AVAILABLE = "Available"
    OCCUPIED = "Occupied"
    RESERVED = "Reserved"  # Can be extended if needed


# Car class
class Car:
    def __init__(self, car_id: str, size: CarSize):
        self.car_id: str = car_id
        self.size: CarSize = size


# ParkingSpace class
class ParkingSpace:
    def __init__(self, space_id: str, size: CarSize, status: SpaceStatus = SpaceStatus.AVAILABLE):
        self.space_id: str = space_id
        self.size: CarSize = size
        self.status: SpaceStatus = status


# ParkingTicket class
class ParkingTicket:
    def __init__(self, ticket_id: str, car_id: str, space_id: Optional[str] = None):
        self.ticket_id: str = ticket_id
        self.car_id: str = car_id
        self.space_id: Optional[str] = space_id
        self.issued_at: Optional[str] = None
        self.checked_out_at: Optional[str] = None


# ParkingLot class
class ParkingLot:
    def __init__(self):
        # Parking spaces organized by size
        self.small_spaces: List[ParkingSpace] = []
        self.medium_spaces: List[ParkingSpace] = []
        self.large_spaces: List[ParkingSpace] = []

        # Dictionary for quick lookup of available spaces by size
        self.available_spaces: Dict[CarSize, int] = {
            CarSize.SMALL: 50,
            CarSize.MEDIUM: 100,
            CarSize.LARGE: 30,
        }

        # Active parking tickets
        self.active_tickets: Dict[str, ParkingTicket] = {}

        # Mapping of car IDs to their current tickets
        self.car_to_ticket: Dict[str, ParkingTicket] = {}

    # Attributes for parking statistics
    def get_total_spaces(self) -> Dict[CarSize, int]:
        """
        Total parking spaces for each size.
        """
        return {
            CarSize.SMALL: 50,
            CarSize.MEDIUM: 100,
            CarSize.LARGE: 30,
        }

    def get_available_spaces(self) -> Dict[CarSize, int]:
        """
        Get the number of available spaces for each size.
        """
        pass

    def get_occupied_spaces(self) -> Dict[CarSize, int]:
        """
        Get the number of occupied spaces for each size.
        """
        pass

    # Methods for car check-in and check-out
    def check_in_car(self, car: Car) -> ParkingTicket:
        """
        Check in a car and assign a parking space.
        Returns a parking ticket.
        """
        pass

    def check_out_car(self, ticket_id: str) -> Optional[ParkingSpace]:
        """
        Check out a car using the ticket ID.
        Frees up the parking space.
        """
        pass

    # Ticket-related methods
    def get_ticket(self, ticket_id: str) -> Optional[ParkingTicket]:
        """
        Retrieve details of a specific parking ticket.
        """
        pass

    # Lift and assignment system
    def assign_space(self, car: Car) -> Optional[ParkingSpace]:
        """
        Assign the most appropriate space for the car.
        """
        pass

    def release_space(self, space_id: str):
        """
        Mark a parking space as available.
        """
        pass

    # Reporting and monitoring
    def generate_report(self) -> Dict[str, int]:
        """
        Generate a report of the parking lot status.
        """
        pass


# ### **API Design in Text Format**
# ```
# POST /cars/
# - Add a car to the system.
# - Request body: { "car_id": "string", "size": "enum (Small, Medium, Large)" }
# - Response: { "message": "Car added successfully." }

# POST /checkin/
# - Check in a car and assign a parking space.
# - Request body: { "car_id": "string" }
# - Response: { "ticket_id": "string", "space_id": "string" }

# POST /checkout/
# - Check out a car using the ticket ID.
# - Request body: { "ticket_id": "string" }
# - Response: { "message": "Car checked out successfully." }

# GET /spaces/
# - Get the count of available parking spaces for a given car size.
# - Query parameter: size=Small/Medium/Large
# - Response: { "size": "string", "available_spaces": "integer" }

# GET /tickets/{ticket_id}/
# - Get details of a specific parking ticket.
# - Path parameter: ticket_id
# - Response: { "ticket_id": "string", "car_id": "string", "space_id": "string", "issued_at": "string", "checked_out_at": "string" }

# GET /report/
# - Get a report of parking lot status (e.g., available spaces, occupied spaces).
# - Response: { "small_spaces": "integer", "medium_spaces": "integer", "large_spaces": "integer", "total_spaces": "integer", "occupied_spaces": "integer" }
# ```

# ---

# ### **Database Schema**
# 1. **Cars Table**
#    - `car_id` (Primary Key): Unique identifier for a car.
#    - `size` (Enum): Size of the car (Small, Medium, Large).

# 2. **ParkingSpaces Table**
#    - `space_id` (Primary Key): Unique identifier for a parking space.
#    - `size` (Enum): Size of the parking space (Small, Medium, Large).
#    - `is_occupied` (Boolean): Whether the space is occupied.

# 3. **ParkingTickets Table**
#    - `ticket_id` (Primary Key): Unique identifier for a parking ticket.
#    - `car_id` (Foreign Key): References the `Cars` table.
#    - `space_id` (Foreign Key): References the `ParkingSpaces` table.
#    - `issued_at` (Timestamp): Time when the ticket was issued.
#    - `checked_out_at` (Timestamp): Time when the car was checked out.

# ---

# ### **Entity Relationship Diagram (ERD)**
# - **Cars** table has a one-to-one relationship with **ParkingTickets**.
# - **ParkingSpaces** table has a one-to-one relationship with **ParkingTickets**.
# - The **ParkingTickets** table serves as the linking table for cars and spaces.

# Let me know if you need further refinements or diagrams!