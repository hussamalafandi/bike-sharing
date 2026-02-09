"""
Custom sorting and searching algorithms.

Provided:
    - merge_sort
    - benchmark_sort

Students must implement:
    - insertion_sort   — second sorting algorithm
    - binary_search    — search on sorted data
    - linear_search    — brute-force search for comparison
    - benchmark_search — timing comparison for search algorithms

Use timeit to measure execution times.
Document the Big-O complexity of each algorithm.
"""

import timeit
from collections.abc import Callable
from typing import Any


# ---------------------------------------------------------------------------
# Sorting — Merge Sort
# ---------------------------------------------------------------------------

def merge_sort(data: list[Any], key: Callable = lambda x: x) -> list[Any]:
    """Sort *data* using the merge-sort algorithm.

    Args:
        data: List of items to sort.
        key: Function that extracts a comparison key from each item.

    Returns:
        A new sorted list.

    Complexity:
        Time  — O(n log n)
        Space — O(n)
    """
    if len(data) <= 1:
        return list(data)

    mid = len(data) // 2
    left = merge_sort(data[:mid], key=key)
    right = merge_sort(data[mid:], key=key)

    return _merge(left, right, key=key)


def _merge(
    left: list[Any], right: list[Any], key: Callable
) -> list[Any]:
    """Merge two sorted lists into one sorted list."""
    result: list[Any] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------------------------------------------------------------------
# Sorting — Insertion Sort (TODO)
# ---------------------------------------------------------------------------

def insertion_sort(data: list[Any], key: Callable = lambda x: x) -> list[Any]:
    """Sort *data* using the insertion-sort algorithm.

    Args:
        data: List of items to sort.
        key: Function that extracts a comparison key from each item.

    Returns:
        A new sorted list (the original is not modified).

    Complexity:
        Time  — O(n²) worst / average, O(n) best (already sorted)
        Space — O(n) for the copy

    TODO:
        - Copy the input list
        - Iterate from index 1 to len(data)
        - For each element, shift larger elements to the right
        - Insert the current element at the correct position
    """
    raise NotImplementedError("insertion_sort")


# ---------------------------------------------------------------------------
# Searching — Binary Search (TODO)
# ---------------------------------------------------------------------------

def binary_search(
    sorted_data: list[Any],
    target: Any,
    key: Callable = lambda x: x,
) -> int | None:
    """Search for *target* in a sorted list using binary search.

    Args:
        sorted_data: A list sorted in ascending order by *key*.
        target: The value to search for.
        key: Function that extracts the comparison value from each item.

    Returns:
        The index of the found item, or None if not found.

    Complexity:
        Time  — O(log n)
        Space — O(1)

    TODO: implement the binary search loop.
    """
    low, high = 0, len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = key(sorted_data[mid])

        # TODO: compare mid_val with target and adjust low/high
        # ----- your code here -----
        pass

    return None


# ---------------------------------------------------------------------------
# Searching — Linear Search (TODO)
# ---------------------------------------------------------------------------

def linear_search(
    data: list[Any],
    target: Any,
    key: Callable = lambda x: x,
) -> int | None:
    """Search for *target* by scanning every element in *data*.

    Args:
        data: List of items (does not need to be sorted).
        target: The value to search for.
        key: Function that extracts the comparison value from each item.

    Returns:
        The index of the first matching item, or None if not found.

    Complexity:
        Time  — O(n)
        Space — O(1)

    TODO: implement the linear scan.
    """
    raise NotImplementedError("linear_search")


# ---------------------------------------------------------------------------
# Benchmarking helper
# ---------------------------------------------------------------------------

def benchmark_sort(data: list, key: Callable = lambda x: x, repeats: int = 5) -> dict:
    """Compare custom merge_sort vs. built-in sorted().

    Returns:
        A dict with 'merge_sort_ms' and 'builtin_sorted_ms' timings.
    """
    custom_time = timeit.timeit(
        lambda: merge_sort(data, key=key), number=repeats
    )
    builtin_time = timeit.timeit(
        lambda: sorted(data, key=key), number=repeats
    )

    return {
        "merge_sort_ms": round(custom_time / repeats * 1000, 2),
        "builtin_sorted_ms": round(builtin_time / repeats * 1000, 2),
    }


def benchmark_search(
    data: list,
    target: Any,
    key: Callable = lambda x: x,
    repeats: int = 5,
) -> dict:
    """Compare custom binary_search vs. built-in methods.

    *data* must already be sorted by *key* for binary_search.

    Returns:
        A dict with 'binary_search_ms', 'linear_search_ms',
        and 'builtin_in_ms' timings.

    TODO: implement once binary_search and linear_search are complete.
    """
    raise NotImplementedError("benchmark_search")
