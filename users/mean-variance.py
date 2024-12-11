import math

def read_numbers_from_file(file_path):
    """Reads numbers from a file and returns them as a list."""
    try:
        with open(file_path, "r") as file:
            numbers = [float(line.strip()) for line in file if line.strip().isdigit() or is_number(line.strip())]
        return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except ValueError:
        print("Error: The file contains invalid numbers.")
        return []

def is_number(value):
    """Checks if a string can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    """Calculates the variance of a list of numbers."""
    if not numbers:
        return 0
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    """Calculates the standard deviation from the variance."""
    return math.sqrt(variance)

def main():
    file_path = input("Enter the path to the file containing numbers: ")
    numbers = read_numbers_from_file(file_path)

    if numbers:
        mean = calculate_mean(numbers)
        variance = calculate_variance(numbers, mean)
        stddev = calculate_standard_deviation(variance)
        minimum = min(numbers)
        maximum = max(numbers)

        print(f"Mean: {mean}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {stddev}")
        print(f"Min: {minimum}")
        print(f"Maximum: {maximum}")
    else:
        print("No valid numbers found in the file.")

if __name__ == "__main__":
    main()
