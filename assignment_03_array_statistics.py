# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of the list using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Return the average of the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    """Return the maximum value in the list using a loop."""
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def calculate_min(numbers):
    """Return the minimum value in the list using a loop."""
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def main():
    # Ask user how many numbers
    n = int(input("How many numbers? "))
    
    if n <= 0:
        print("Error: Number of elements must be positive.")
        return
    
    numbers = []
    for i in range(n):
        value = float(input(f"Enter number {i+1}: "))
        numbers.append(value)
    
    # Compute results
    total = calculate_sum(numbers)
    avg = calculate_average(numbers)
    maximum = calculate_max(numbers)
    minimum = calculate_min(numbers)
    
    # Display results
    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()
    
