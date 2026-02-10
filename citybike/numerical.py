"""
NumPy-based numerical computations for the CityBike platform.

Students should implement:
    - Station distance matrix using Euclidean distance
    - Vectorized trip statistics (mean, median, std, percentiles)
    - Outlier detection using z-scores
    - Vectorized fare calculation across all trips
"""

import numpy as np


# ---------------------------------------------------------------------------
# Distance calculations
# ---------------------------------------------------------------------------

def station_distance_matrix(
    latitudes: np.ndarray, longitudes: np.ndarray
) -> np.ndarray:
    """Compute pairwise Euclidean distances between stations.

    Uses a simplified flat-earth distance model:
        d = sqrt((lat2 - lat1)^2 + (lon2 - lon1)^2)

    Args:
        latitudes: 1-D array of station latitudes.
        longitudes: 1-D array of station longitudes.

    Returns:
        A 2-D symmetric distance matrix of shape (n, n).

    TODO: implement using NumPy broadcasting (no Python loops).

    Hints:
        1. Reshape latitudes to a column vector: latitudes[:, np.newaxis]  → shape (n, 1)
        2. Subtracting the original row vector gives all pairwise differences:
               lat_diff = latitudes[:, np.newaxis] - latitudes[np.newaxis, :]  → shape (n, n)
        3. Do the same for longitudes.
        4. Apply the formula: np.sqrt(lat_diff**2 + lon_diff**2)
    """
    # Step 1: compute pairwise latitude differences
    # lat_diff = latitudes[:, np.newaxis] - latitudes[np.newaxis, :]

    # Step 2: compute pairwise longitude differences
    # lon_diff = ...

    # Step 3: combine with Euclidean formula
    # np.sqrt(lat_diff**2 + lon_diff**2)

    raise NotImplementedError("station_distance_matrix")


# ---------------------------------------------------------------------------
# Trip statistics
# ---------------------------------------------------------------------------

def trip_duration_stats(durations: np.ndarray) -> dict[str, float]:
    """Compute summary statistics for trip durations.

    Args:
        durations: 1-D array of trip durations in minutes.

    Returns:
        Dict with keys: mean, median, std, p25, p75, p90.

    TODO: use NumPy functions (np.mean, np.median, np.std, np.percentile).
    """
    # Example (partially done):
    return {
        "mean": float(np.mean(durations)),
        "median": float(np.median(durations)),
        "std": float(np.std(durations)),
        # TODO: add p25, p75, p90 using np.percentile
    }


# ---------------------------------------------------------------------------
# Outlier detection
# ---------------------------------------------------------------------------

def detect_outliers_zscore(
    values: np.ndarray, threshold: float = 3.0
) -> np.ndarray:
    """Identify outlier indices using the z-score method.

    An observation is an outlier if |z| > threshold.

    Args:
        values: 1-D array of numeric values.
        threshold: Z-score cutoff (default 3.0).

    Returns:
        Boolean array — True where the value is an outlier.

    TODO: compute z-scores and return the boolean mask.

    Hints:
        1. Compute the mean:  mean = np.mean(values)
        2. Compute the std:   std  = np.std(values)
        3. Guard against std == 0 (return all-False array)
        4. Compute z-scores:  z = (values - mean) / std
        5. Return boolean:    np.abs(z) > threshold
    """

    raise NotImplementedError("detect_outliers_zscore")


# ---------------------------------------------------------------------------
# Vectorized fare calculation
# ---------------------------------------------------------------------------

def calculate_fares(
    durations: np.ndarray,
    distances: np.ndarray,
    per_minute: float,
    per_km: float,
    unlock_fee: float = 0.0,
) -> np.ndarray:
    """Calculate fares for many trips at once using NumPy.

    Args:
        durations: 1-D array of trip durations (minutes).
        distances: 1-D array of trip distances (km).
        per_minute: Cost per minute.
        per_km: Cost per km.
        unlock_fee: Flat unlock fee (default 0).

    Returns:
        1-D array of trip fares.

    TODO: implement a single vectorized expression (no loops).

    Hints:
        The fare for a single trip is:
            fare = unlock_fee + (per_minute * duration) + (per_km * distance)

        With NumPy, you can compute this for ALL trips at once because
        arithmetic on arrays is element-wise:
            fares = unlock_fee + per_minute * durations + per_km * distances

        This single line replaces a Python for-loop over every trip.

    Example:
        >>> durations = np.array([10, 20, 30])
        >>> distances = np.array([2.0, 5.0, 8.0])
        >>> calculate_fares(durations, distances, per_minute=0.15, per_km=0.10, unlock_fee=1.0)
        array([2.7, 4.5, 6.3])
        # trip 1: 1.0 + 0.15*10 + 0.10*2.0 = 2.70
        # trip 2: 1.0 + 0.15*20 + 0.10*5.0 = 4.50
        # trip 3: 1.0 + 0.15*30 + 0.10*8.0 = 6.30
    """

    raise NotImplementedError("calculate_fares")
