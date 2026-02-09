"""
Custom sorting and searching algorithms.

Students must implement:
    1. At least one sorting algorithm from scratch (e.g., merge sort)
    2. At least one searching algorithm from scratch (e.g., binary search)
    3. Benchmarks comparing custom vs. built-in implementations

Use timeit to measure execution times.
Document the Big-O complexity of each algorithm.
"""

import timeit
from collections.abc import Callable
from typing import Any


# ---------------------------------------------------------------------------
# Sorting — Merge Sort (example skeleton)
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

    TODO:
        - Implement the divide step (split list in half)
        - Implement the merge step (combine two sorted halves)
        - Return the fully sorted list
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
    """Merge two sorted lists into one sorted list.

    TODO: implement the merge logic.
    """
    result: list[Any] = []
    i = j = 0

    # TODO: compare elements from left and right using key(),
    #       append the smaller one to result, advance the pointer.
    # ----- your code here -----

    # TODO: append any remaining elements from left or right
    # ----- your code here -----

    return result


# ---------------------------------------------------------------------------
# Searching — Binary Search (example skeleton)
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
# Benchmarking helper
# ---------------------------------------------------------------------------

def benchmark_sort(data: list, key: Callable = lambda x: x, repeats: int = 5) -> dict:
    """Compare custom merge_sort vs. built-in sorted().

    Returns:
        A dict with 'merge_sort_ms' and 'builtin_sorted_ms' timings.

    TODO: complete the timing calls using timeit.repeat or timeit.timeit
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
