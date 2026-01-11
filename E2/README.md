# Median Finder Program

A Python implementation that sorts an array of numbers and finds the median value using the Bubble Sort algorithm.

## Overview

This program converts pseudocode into a working Python application that:
- Implements a sorting algorithm (Bubble Sort)
- Calculates the median of an array of numbers
- Provides both predefined test cases and user input functionality

## Features

- ✅ **Custom Sorting Implementation**: Uses optimized Bubble Sort algorithm
- ✅ **Median Calculation**: Correctly handles both odd and even-length arrays
- ✅ **Predefined Test Cases**: 5 comprehensive test cases demonstrating various scenarios
- ✅ **Interactive User Input**: Allows users to input their own arrays
- ✅ **Error Handling**: Validates user input and handles edge cases
- ✅ **Clean, Readable Code**: Well-documented with docstrings and comments

## Algorithm Details

### Sorting Algorithm: Bubble Sort

The implementation uses an optimized Bubble Sort with the following characteristics:
- **Time Complexity**: O(n²) worst case, O(n) best case (when array is already sorted)
- **Space Complexity**: O(1) - sorts in place
- **Optimization**: Early termination when no swaps occur

### Median Calculation

- **Even-length arrays**: Returns the average of the two middle elements
- **Odd-length arrays**: Returns the middle element

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd E2
```

2. No additional dependencies required - uses only Python standard library

## Usage

### Running the Program

```bash
python3 median_finder.py
```

### Program Flow

1. **Predefined Test Cases**: The program first runs 5 test cases automatically:
   - Mixed positive integers
   - Even-length array
   - Single element array
   - Floating-point numbers
   - Larger array

2. **User Input Mode**: After test cases, you can enter your own arrays:
   - Enter numbers separated by spaces
   - Type 'q' to quit

### Example Usage

```
Enter numbers separated by spaces (or 'q' to quit): 15 3 9 21 7

Original Array: [15.0, 3.0, 9.0, 21.0, 7.0]
Sorted Array:   [3.0, 7.0, 9.0, 15.0, 21.0]
Median:         9.0
```

## Test Cases

The program includes the following predefined test cases:

| Test Case | Input | Sorted | Median |
|-----------|-------|--------|--------|
| 1 | [7, 2, 9, 4, 5] | [2, 4, 5, 7, 9] | 5 |
| 2 | [10, 20, 30, 40] | [10, 20, 30, 40] | 25.0 |
| 3 | [5] | [5] | 5 |
| 4 | [3.5, 1.2, 4.8, 2.1, 6.3, 5.5] | [1.2, 2.1, 3.5, 4.8, 5.5, 6.3] | 4.15 |
| 5 | [100, 50, 75, 25, 10, 90, 60] | [10, 25, 50, 60, 75, 90, 100] | 60 |

## Code Structure

```
median_finder.py
├── sort(numbers)           # Implements Bubble Sort algorithm
├── sortAndFindMedian(numbers)  # Sorts and finds median
└── main()                  # Main program with test cases and UI
```

## Implementation Details

### Key Functions

#### `sort(numbers)`
- Implements optimized Bubble Sort
- Sorts array in ascending order in-place
- Returns sorted array

#### `sortAndFindMedian(numbers)`
- Calls `sort()` to sort the array
- Calculates median based on array length
- Returns median value as float

#### `main()`
- Runs predefined test cases
- Provides interactive user input interface
- Handles errors and validates input

## Edge Cases Handled

- ✅ Single element arrays
- ✅ Even and odd length arrays
- ✅ Floating-point numbers
- ✅ Already sorted arrays
- ✅ Reverse sorted arrays
- ✅ Invalid user input
- ✅ Empty input

## Author

Created as part of a programming exercise to convert pseudocode into a working implementation.

## License

This project is open source and available for educational purposes.
