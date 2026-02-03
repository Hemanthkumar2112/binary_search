from __future__ import annotations

from typing import Iterable, Sequence


def binary_search(values: Sequence[int], target: int) -> int:
    """Return the index of target in a sorted sequence or -1 if not found."""
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = values[mid]

        if mid_value == target:
            return mid
        if mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_in_unsorted(values: Iterable[int], target: int) -> int:
    """Search an unsorted iterable by sorting once, returning the original index."""
    indexed_values = sorted(enumerate(values), key=lambda item: item[1])
    sorted_values = [value for _, value in indexed_values]
    sorted_index = binary_search(sorted_values, target)
    if sorted_index == -1:
        return -1
    return indexed_values[sorted_index][0]


if __name__ == "__main__":
    data = [10, 4, 7, 2, 19, 3]
    target = 7

    sorted_data = sorted(data)
    sorted_index = binary_search(sorted_data, target)
    unsorted_index = binary_search_in_unsorted(data, target)

    if sorted_index != -1:
        print(f"Found {target} in sorted data at index {sorted_index}.")
    else:
        print(f"{target} not found in sorted data.")

    if unsorted_index != -1:
        print(f"Found {target} in original data at index {unsorted_index}.")
    else:
        print(f"{target} not found in original data.")
