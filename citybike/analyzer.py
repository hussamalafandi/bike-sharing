"""
Data analysis engine for the CityBike platform.

Contains the BikeShareSystem class that orchestrates:
    - CSV loading and cleaning
    - Answering business questions using Pandas
    - Generating summary reports

Students should implement the cleaning logic and at least 10 analytics methods.
"""

import pandas as pd
import numpy as np
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"


class BikeShareSystem:
    """Central analysis class — loads, cleans, and analyzes bike-share data.

    Attributes:
        trips: DataFrame of trip records.
        stations: DataFrame of station metadata.
        maintenance: DataFrame of maintenance records.
    """

    def __init__(self) -> None:
        self.trips: pd.DataFrame | None = None
        self.stations: pd.DataFrame | None = None
        self.maintenance: pd.DataFrame | None = None

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def load_data(self) -> None:
        """Load raw CSV files into DataFrames."""
        self.trips = pd.read_csv(DATA_DIR / "trips.csv")
        self.stations = pd.read_csv(DATA_DIR / "stations.csv")
        self.maintenance = pd.read_csv(DATA_DIR / "maintenance.csv")
        print(f"Loaded trips: {self.trips.shape}")
        print(f"Loaded stations: {self.stations.shape}")
        print(f"Loaded maintenance: {self.maintenance.shape}")

    # ------------------------------------------------------------------
    # Data inspection (provided)
    # ------------------------------------------------------------------

    def inspect_data(self) -> None:
        """Print basic info about each DataFrame."""
        for name, df in [
            ("Trips", self.trips),
            ("Stations", self.stations),
            ("Maintenance", self.maintenance),
        ]:
            print(f"\n{'='*40}")
            print(f"  {name}")
            print(f"{'='*40}")
            print(df.info())
            print(f"\nMissing values:\n{df.isnull().sum()}")
            print(f"\nFirst 3 rows:\n{df.head(3)}")

    # ------------------------------------------------------------------
    # Data cleaning
    # ------------------------------------------------------------------

    def clean_data(self) -> None:
        """Clean all DataFrames and export to CSV.

        Steps to implement:
            1. Remove duplicate rows
            2. Parse date/datetime columns
            3. Convert numeric columns stored as strings
            4. Handle missing values (document your strategy!)
            5. Remove invalid entries (e.g. end_time < start_time)
            6. Standardize categorical values
            7. Export cleaned data to data/trips_clean.csv etc.

        TODO: implement each step below.
        """
        if self.trips is None:
            raise RuntimeError("Call load_data() first")

        # --- Step 1: Remove duplicates ---
        self.trips = self.trips.drop_duplicates(subset=["trip_id"])
        print(f"After dedup: {self.trips.shape[0]} trips")

        # --- Step 2: Parse dates ---
        # TODO: convert start_time, end_time to datetime
        # self.trips["start_time"] = pd.to_datetime(...)

        # --- Step 3: Convert numeric columns ---
        # TODO: ensure duration_minutes and distance_km are float

        # --- Step 4: Handle missing values ---
        # TODO: decide on a strategy and document it
        # Example: self.trips["duration_minutes"].fillna(..., inplace=True)

        # --- Step 5: Remove invalid entries ---
        # TODO: drop rows where end_time < start_time

        # --- Step 6: Standardize categoricals ---
        # TODO: e.g. self.trips["status"].str.lower().str.strip()

        # --- Step 7: Export cleaned datasets ---
        # self.trips.to_csv(DATA_DIR / "trips_clean.csv", index=False)
        # self.stations.to_csv(DATA_DIR / "stations_clean.csv", index=False)

        print("Cleaning complete.")

    # ------------------------------------------------------------------
    # Analytics — Business Questions
    # ------------------------------------------------------------------

    def total_trips_summary(self) -> dict:
        """Q1: Total trips, total distance, average duration.

        Returns:
            Dict with 'total_trips', 'total_distance_km', 'avg_duration_min'.
        """
        df = self.trips
        return {
            "total_trips": len(df),
            "total_distance_km": round(df["distance_km"].sum(), 2),
            "avg_duration_min": round(df["duration_minutes"].mean(), 2),
        }

    def top_start_stations(self, n: int = 10) -> pd.DataFrame:
        """Q2: Top *n* most popular start stations.

        TODO: use value_counts() or groupby on start_station_id,
              merge with station names.
        """
        # Example start:
        # counts = self.trips["start_station_id"].value_counts().head(n)
        raise NotImplementedError("top_start_stations")

    def peak_usage_hours(self) -> pd.Series:
        """Q3: Trip count by hour of day.

        TODO: extract hour from start_time and count trips per hour.
        """
        raise NotImplementedError("peak_usage_hours")

    def busiest_day_of_week(self) -> pd.Series:
        """Q4: Trip count by day of week.

        TODO: extract day-of-week from start_time, count.
        """
        raise NotImplementedError("busiest_day_of_week")

    def avg_distance_by_user_type(self) -> pd.Series:
        """Q5: Average trip distance grouped by user type."""
        raise NotImplementedError("avg_distance_by_user_type")

    def monthly_trip_trend(self) -> pd.Series:
        """Q7: Monthly trip counts over time.

        TODO: extract year-month from start_time, group, count.
        """
        raise NotImplementedError("monthly_trip_trend")

    def top_active_users(self, n: int = 15) -> pd.DataFrame:
        """Q8: Top *n* most active users by trip count.

        TODO: group by user_id, count trips, sort descending.
        """
        raise NotImplementedError("top_active_users")

    def maintenance_cost_by_bike_type(self) -> pd.Series:
        """Q9: Total maintenance cost per bike type.

        TODO: group maintenance by bike_type, sum cost.
        """
        raise NotImplementedError("maintenance_cost_by_bike_type")

    def top_routes(self, n: int = 10) -> pd.DataFrame:
        """Q10: Most common start→end station pairs.

        TODO: group by (start_station_id, end_station_id), count, sort.
        """
        raise NotImplementedError("top_routes")

    # ------------------------------------------------------------------
    # Add more analytics methods here (Q6, Q11–Q14)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def generate_summary_report(self) -> None:
        """Write a summary text report to output/summary_report.txt.

        TODO:
            - Call each analytics method
            - Format the results as readable text
            - Write to file
        """
        raise NotImplementedError("generate_summary_report")
