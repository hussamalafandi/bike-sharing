"""
Domain models for the CityBike Bike-Sharing Analytics platform.

This module defines the class hierarchy:
    Entity (ABC) -> Bike -> ClassicBike, ElectricBike
                 -> Station
                 -> User -> CasualUser, MemberUser
    Trip
    MaintenanceRecord
    BikeShareSystem

TODO for students:
    - Complete the Station, User, CasualUser, MemberUser classes
    - Complete the Trip and MaintenanceRecord classes
    - Implement the BikeShareSystem class
    - Add input validation to all constructors
    - Add @property decorators where appropriate
"""

from abc import ABC, abstractmethod
from datetime import datetime


# ---------------------------------------------------------------------------
# Abstract Base Class
# ---------------------------------------------------------------------------

class Entity(ABC):
    """Abstract base class for all domain entities.

    Attributes:
        id: Unique identifier for the entity.
        created_at: Timestamp when the entity was created.
    """

    def __init__(self, id: str, created_at: datetime | None = None) -> None:
        if not id or not isinstance(id, str):
            raise ValueError("id must be a non-empty string")
        self._id = id
        self._created_at = created_at or datetime.now()

    @property
    def id(self) -> str:
        """Return the entity's unique identifier."""
        return self._id

    @property
    def created_at(self) -> datetime:
        """Return the creation timestamp."""
        return self._created_at

    @abstractmethod
    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """Return an unambiguous string representation for debugging."""
        ...


# ---------------------------------------------------------------------------
# Bike hierarchy
# ---------------------------------------------------------------------------

class Bike(Entity):
    """Represents a bike in the sharing system.

    Attributes:
        bike_type: Either 'classic' or 'electric'.
        status: One of 'available', 'in_use', 'maintenance'.
    """

    VALID_STATUSES = {"available", "in_use", "maintenance"}

    def __init__(
        self,
        bike_id: str,
        bike_type: str,
        status: str = "available",
    ) -> None:
        super().__init__(id=bike_id)
        if bike_type not in ("classic", "electric"):
            raise ValueError(f"Invalid bike_type: {bike_type}")
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}")
        self._bike_type = bike_type
        self._status = status

    @property
    def bike_type(self) -> str:
        return self._bike_type

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {value}")
        self._status = value

    def __str__(self) -> str:
        return f"Bike({self.id}, {self.bike_type}, {self.status})"

    def __repr__(self) -> str:
        return (
            f"Bike(bike_id={self.id!r}, bike_type={self.bike_type!r}, "
            f"status={self.status!r})"
        )


class ClassicBike(Bike):
    """A classic (non-electric) bike with gears.

    Attributes:
        gear_count: Number of gears (must be positive).
    """

    def __init__(
        self,
        bike_id: str,
        gear_count: int = 7,
        status: str = "available",
    ) -> None:
        super().__init__(bike_id=bike_id, bike_type="classic", status=status)
        if gear_count <= 0:
            raise ValueError("gear_count must be positive")
        self._gear_count = gear_count

    @property
    def gear_count(self) -> int:
        return self._gear_count

    def __str__(self) -> str:
        return f"ClassicBike({self.id}, gears={self.gear_count})"

    def __repr__(self) -> str:
        return (
            f"ClassicBike(bike_id={self.id!r}, gear_count={self.gear_count}, "
            f"status={self.status!r})"
        )


class ElectricBike(Bike):
    """An electric bike with a battery.

    TODO:
        - Add battery_level (float, 0–100) and max_range_km (float, > 0)
        - Validate inputs in __init__
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        bike_id: str,
        battery_level: float = 100.0,
        max_range_km: float = 50.0,
        status: str = "available",
    ) -> None:
        super().__init__(bike_id=bike_id, bike_type="electric", status=status)
        # TODO: validate battery_level (0-100) and max_range_km (>0)
        # TODO: store as private attributes with @property access
        pass

    def __str__(self) -> str:
        # TODO: return a user-friendly string
        return f"ElectricBike({self.id})"

    def __repr__(self) -> str:
        # TODO: return a debug-friendly string
        return f"ElectricBike(bike_id={self.id!r})"


# ---------------------------------------------------------------------------
# Station
# ---------------------------------------------------------------------------

class Station(Entity):
    """Represents a bike-sharing station.

    TODO:
        - Store station_id, name, capacity, latitude, longitude
        - Validate: capacity > 0, lat in [-90, 90], lon in [-180, 180]
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        station_id: str,
        name: str,
        capacity: int,
        latitude: float,
        longitude: float,
    ) -> None:
        super().__init__(id=station_id)
        # TODO: validate and store attributes
        pass

    def __str__(self) -> str:
        # TODO
        return f"Station({self.id})"

    def __repr__(self) -> str:
        # TODO
        return f"Station(station_id={self.id!r})"


# ---------------------------------------------------------------------------
# User hierarchy
# ---------------------------------------------------------------------------

class User(Entity):
    """Base class for a system user.

    TODO:
        - Store user_id, name, email, user_type
        - Validate email format (basic check: contains '@')
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        user_type: str,
    ) -> None:
        super().__init__(id=user_id)
        # TODO: validate and store attributes
        pass

    def __str__(self) -> str:
        # TODO
        return f"User({self.id})"

    def __repr__(self) -> str:
        # TODO
        return f"User(user_id={self.id!r})"


class CasualUser(User):
    """A casual (non-member) user.

    TODO:
        - Add day_pass_count (int >= 0)
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        day_pass_count: int = 0,
    ) -> None:
        super().__init__(user_id=user_id, name=name, email=email, user_type="casual")
        # TODO: validate and store day_pass_count
        pass

    def __str__(self) -> str:
        # TODO
        return f"CasualUser({self.id})"

    def __repr__(self) -> str:
        # TODO
        return f"CasualUser(user_id={self.id!r})"


class MemberUser(User):
    """A registered member user.

    TODO:
        - Add membership_start (datetime), membership_end (datetime), tier (basic/premium)
        - Validate that membership_end > membership_start
        - Validate tier is 'basic' or 'premium'
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        membership_start: datetime = None,
        membership_end: datetime = None,
        tier: str = "basic",
    ) -> None:
        super().__init__(user_id=user_id, name=name, email=email, user_type="member")
        # TODO: validate and store attributes
        pass

    def __str__(self) -> str:
        # TODO
        return f"MemberUser({self.id})"

    def __repr__(self) -> str:
        # TODO
        return f"MemberUser(user_id={self.id!r})"


# ---------------------------------------------------------------------------
# Trip
# ---------------------------------------------------------------------------

class Trip:
    """Represents a single bike trip.

    TODO:
        - Store all attributes: trip_id, user, bike, start_station,
          end_station, start_time, end_time, distance_km
        - Validate: distance_km >= 0, end_time >= start_time
        - Implement duration_minutes as a @property
        - Implement __str__ and __repr__
    """

    def __init__(
        self,
        trip_id: str,
        user: User,
        bike: Bike,
        start_station: Station,
        end_station: Station,
        start_time: datetime,
        end_time: datetime,
        distance_km: float,
    ) -> None:
        # TODO: validate and store attributes
        pass

    @property
    def duration_minutes(self) -> float:
        """Calculate trip duration in minutes from start and end times."""
        # TODO: compute from end_time - start_time
        return 0.0

    def __str__(self) -> str:
        # TODO
        return f"Trip({self.trip_id})"

    def __repr__(self) -> str:
        # TODO
        return f"Trip(trip_id={self.trip_id!r})"


# ---------------------------------------------------------------------------
# MaintenanceRecord
# ---------------------------------------------------------------------------

class MaintenanceRecord:
    """Represents a maintenance event for a bike.

    TODO:
        - Store: record_id, bike, date, maintenance_type, cost, description
        - Validate: cost >= 0, maintenance_type is one of the allowed types
        - Implement __str__ and __repr__
    """

    VALID_TYPES = {
        "tire_repair",
        "brake_adjustment",
        "battery_replacement",
        "chain_lubrication",
        "general_inspection",
    }

    def __init__(
        self,
        record_id: str,
        bike: Bike,
        date: datetime,
        maintenance_type: str,
        cost: float,
        description: str = "",
    ) -> None:
        # TODO: validate and store attributes
        pass

    def __str__(self) -> str:
        # TODO
        return "MaintenanceRecord()"

    def __repr__(self) -> str:
        # TODO
        return "MaintenanceRecord()"
