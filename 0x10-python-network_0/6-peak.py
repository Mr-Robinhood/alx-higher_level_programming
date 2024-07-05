def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    
    Args:
    - list_of_integers: A list of unsorted integers
    
    Returns:
    - A peak element from the list
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        
        # If the left neighbor is greater, search left
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        # Otherwise, search right
        else:
            low = mid + 1
    
    # Return the peak (in case the list has only one element)
    return list_of_integers[low]

