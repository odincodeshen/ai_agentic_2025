"""
Bubble Sort Implementation in Python

Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until no swaps are needed.

Time Complexity: O(n²) - worst and average case
Space Complexity: O(1) - in-place sorting
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm
    
    Args:
        arr (list): List of comparable elements to sort
        
    Returns:
        list: Sorted list
        
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm - if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap if they are in wrong order
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr_copy


def bubble_sort_verbose(arr):
    """
    Bubble sort with detailed step-by-step output for educational purposes
    
    Args:
        arr (list): List of comparable elements to sort
        
    Returns:
        list: Sorted list
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    print(f"Original array: {arr_copy}")
    print("Starting bubble sort...")
    
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr_copy[j]} and {arr_copy[j + 1]}", end=" ")
            
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap elements
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                print(f"-> Swapped: {arr_copy}")
                swapped = True
            else:
                print(f"-> No swap needed")
        
        if not swapped:
            print(f"  No swaps in pass {i + 1}, array is sorted!")
            break
    
    print(f"\nFinal sorted array: {arr_copy}")
    return arr_copy


def bubble_sort_recursive(arr, n=None):
    """
    Recursive implementation of bubble sort
    
    Args:
        arr (list): List of comparable elements to sort
        n (int): Length of array (used internally for recursion)
        
    Returns:
        list: Sorted list
    """
    if n is None:
        n = len(arr)
        arr = arr.copy()
    
    # Base case: if array has 1 element, it's sorted
    if n == 1:
        return arr
    
    # One pass of bubble sort - move largest element to end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursively sort the remaining n-1 elements
    return bubble_sort_recursive(arr, n - 1)


def optimized_bubble_sort(arr):
    """
    Optimized bubble sort with early termination
    
    Args:
        arr (list): List of comparable elements to sort
        
    Returns:
        list: Sorted list
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        swapped = False
        
        # Reduce the range by i since last i elements are sorted
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    return arr_copy


# Test functions
def test_bubble_sort():
    """Test the bubble sort implementation with various test cases"""
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1.5, 2.3, 0.8, 4.1, 3.2]
    ]
    
    print("Testing Bubble Sort Implementation")
    print("=" * 50)
    
    for i, test_arr in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test_arr}")
        
        # Test regular bubble sort
        sorted_arr = bubble_sort(test_arr)
        print(f"Sorted: {sorted_arr}")
        
        # Verify it's actually sorted
        is_sorted = sorted_arr == sorted(test_arr)
        print(f"Correctly sorted: {is_sorted}")


def demonstrate_verbose_sort():
    """Demonstrate the verbose bubble sort with step-by-step output"""
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Bubble Sort with Step-by-Step Output")
    print("=" * 60)
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_verbose(test_array)


def compare_implementations():
    """Compare different bubble sort implementations"""
    print("\n" + "=" * 60)
    print("COMPARISON: Different Bubble Sort Implementations")
    print("=" * 60)
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Original array: {test_array}")
    
    # Test all implementations
    implementations = [
        ("Regular Bubble Sort", bubble_sort),
        ("Optimized Bubble Sort", optimized_bubble_sort),
        ("Recursive Bubble Sort", bubble_sort_recursive)
    ]
    
    for name, func in implementations:
        result = func(test_array)
        print(f"{name}: {result}")


if __name__ == "__main__":
    # Run all demonstrations
    test_bubble_sort()
    demonstrate_verbose_sort()
    compare_implementations()
    
    print("\n" + "=" * 60)
    print("Bubble Sort Implementation Complete!")
    print("=" * 60) 