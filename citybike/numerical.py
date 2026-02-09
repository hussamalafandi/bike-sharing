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
    """
    # Hint: reshape arrays to (n,1) and (1,n) for broadcasting
    # lat_diff = latitudes[:, np.newaxis] - latitudes[np.newaxis, :]
    # ...
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
    """
    # z = (values - mean) / std
    # return np.abs(z) > threshold
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
    """
    raise NotImplementedError("calculate_fares")
