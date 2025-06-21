# Bubble Sort Implementation in Python

This project contains a comprehensive implementation of the bubble sort algorithm in Python, including multiple variations and educational demonstrations.

## Overview

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed.

## Algorithm Characteristics

- **Time Complexity**: O(n²) - worst and average case
- **Space Complexity**: O(1) - in-place sorting
- **Stability**: Stable (maintains relative order of equal elements)
- **In-place**: Yes (modifies the original array)

## Files

- `bubble_sort.py` - Main implementation with multiple variations and test cases

## Implementations Included

### 1. Basic Bubble Sort (`bubble_sort`)
- Standard implementation with early termination optimization
- Returns a copy of the sorted array (doesn't modify original)

### 2. Verbose Bubble Sort (`bubble_sort_verbose`)
- Educational version with detailed step-by-step output
- Shows each comparison and swap operation
- Perfect for understanding how the algorithm works

### 3. Recursive Bubble Sort (`bubble_sort_recursive`)
- Recursive implementation of the algorithm
- Demonstrates how bubble sort can be implemented recursively

### 4. Optimized Bubble Sort (`optimized_bubble_sort`)
- Enhanced version with early termination
- Stops when no swaps occur in a pass

## Usage

### Basic Usage
```python
from bubble_sort import bubble_sort

# Sort a list
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### Educational Demonstration
```python
from bubble_sort import bubble_sort_verbose

# See step-by-step sorting process
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_verbose(arr)
```

### Run All Tests
```python
python3 bubble_sort.py
```

## Test Cases

The implementation includes comprehensive test cases:
- Random arrays
- Already sorted arrays
- Reverse sorted arrays
- Arrays with duplicate elements
- Empty arrays
- Single element arrays
- Floating point numbers

## How It Works

1. **Outer Loop**: Traverses through all array elements
2. **Inner Loop**: Compares adjacent elements
3. **Swapping**: If elements are in wrong order, swap them
4. **Optimization**: If no swaps occur in a pass, array is sorted
5. **Termination**: Algorithm stops when no swaps are needed

## Example Output

When running the verbose version:
```
Original array: [64, 34, 25, 12, 22, 11, 90]
Starting bubble sort...

Pass 1:
  Comparing 64 and 34 -> Swapped: [34, 64, 25, 12, 22, 11, 90]
  Comparing 64 and 25 -> Swapped: [34, 25, 64, 12, 22, 11, 90]
  ...
  No swaps in pass 7, array is sorted!

Final sorted array: [11, 12, 22, 25, 34, 64, 90]
```

## Educational Value

This implementation is designed for learning purposes and includes:
- Detailed comments explaining each step
- Multiple implementation approaches
- Comprehensive test cases
- Verbose output for understanding the process
- Performance characteristics explanation

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Running the Project

```bash
cd example3
python3 bubble_sort.py
```

This will run all demonstrations including:
- Test cases with various input types
- Step-by-step verbose sorting demonstration
- Comparison of different implementations 