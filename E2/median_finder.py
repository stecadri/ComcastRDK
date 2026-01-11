"""
Median Finder Program
This program implements a sorting algorithm and finds the median of an array of numbers.
"""

def sort(numbers):
    """
    Sorts the numbers array in ascending order using Bubble Sort algorithm.
    
    Args:
        numbers: List of numbers to be sorted
    
    Returns:
        The sorted list (in-place sorting)
    """
    n = len(numbers)
    
    # Bubble Sort implementation
    for i in range(n):
        # Flag to optimize by detecting if array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return numbers


def sortAndFindMedian(numbers):
    """
    Sorts an array of numbers and finds the median value.
    
    Args:
        numbers: List of numbers
    
    Returns:
        The median value of the sorted array
    """
    # Sort the numbers array
    sort(numbers)
    
    # Get the length of the array
    n = len(numbers)
    
    # If even number of elements, return average of two middle elements
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        # If odd number of elements, return the middle element
        return numbers[n // 2]


def main():
    """
    Main function with predefined test cases and user input option.
    """
    print("=" * 60)
    print("MEDIAN FINDER PROGRAM")
    print("=" * 60)
    print()
    
    # Predefined test cases
    test_cases = [
        [7, 2, 9, 4, 5],
        [10, 20, 30, 40],
        [5],
        [3.5, 1.2, 4.8, 2.1, 6.3, 5.5],
        [100, 50, 75, 25, 10, 90, 60]
    ]
    
    print("PREDEFINED TEST CASES:")
    print("-" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        original = test_case.copy()
        median = sortAndFindMedian(test_case)
        print(f"Test Case {i}:")
        print(f"  Original Array: {original}")
        print(f"  Sorted Array:   {test_case}")
        print(f"  Median:         {median}")
        print()
    
    # User input option
    print("=" * 60)
    print("USER INPUT MODE")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\nEnter numbers separated by spaces (or 'q' to quit): ").strip()
            
            if user_input.lower() == 'q':
                print("\nThank you for using the Median Finder Program!")
                break
            
            # Parse the input
            numbers = [float(x) for x in user_input.split()]
            
            if len(numbers) == 0:
                print("Error: Please enter at least one number.")
                continue
            
            # Find median
            original = numbers.copy()
            median = sortAndFindMedian(numbers)
            
            print(f"\nOriginal Array: {original}")
            print(f"Sorted Array:   {numbers}")
            print(f"Median:         {median}")
            
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            break


if __name__ == "__main__":
    main()
