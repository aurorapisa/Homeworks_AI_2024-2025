def binary_search_iterative(sorted_list: list, target: int) -> int:
    """
    Implement iterative binary search
    Args:
        sorted_list: Sorted list of integers
        target: Value to find
    Returns:
        index of target if found, -1 if not found
    """
    left = 0
    right = len(sorted_list) - 1   # the len function in Python is used to calculate the length of the list (in my list from 0 to 8 = 7)

    if not sorted_list:
        print("Empty list. Insert the numbers into the list.")
        return -1

    while left <= right:
        mid = (left + right) // 2   # index
        print(f"Checking range {sorted_list[left:right + 1]}. Middle element is {sorted_list[mid]}")

        if sorted_list[mid] == target:
            print(f"Found target {target} at index {mid}")
            return mid
        elif sorted_list[mid] < target:
            print(f"Target {target} is greater than {sorted_list[mid]}. Moving right.")
            left = mid + 1
        else:
            print(f"Target {target} is less than {sorted_list[mid]}. Moving left.")
            right = mid - 1

    print(f"Target {target} not found in the list.")
    return -1
    pass

def binary_search_recursive(sorted_list: list, target: int, left: int, right: int) -> int:
    """
    Implement recursive binary search
    Args:
        sorted_list: Sorted list of integers
        target: Value to find
        left: Left boundary index
        right: Right boundary index
    Returns:
        index of target if found, -1 if not found
    """
    if left > right:
        print(f"Target {target} not found in the list.")
        return -1

    mid = (left + right) // 2
    print(f"Checking range {sorted_list[left:right + 1]}. Middle element is {sorted_list[mid]}")

    if sorted_list[mid] == target:
        print(f"Found target {target} at index {mid}")
        return mid
    elif sorted_list[mid] < target:
        print(f"Target {target} is greater than {sorted_list[mid]}. Moving right.")
        return binary_search_recursive(sorted_list, target, mid + 1, right)
    else:
        print(f"Target {target} is less than {sorted_list[mid]}. Moving left.")
        return binary_search_recursive(sorted_list, target, left, mid - 1)

    pass