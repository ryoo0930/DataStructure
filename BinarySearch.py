def binary_search(data, target, low, high):
    """Return true if target is found in indicated portion of a Python list."""
    """The search only considers the portion from data[low] to data[high] inclusive"""
    
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)