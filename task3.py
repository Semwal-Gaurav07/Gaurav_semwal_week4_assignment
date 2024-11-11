import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def read_file(file_path):
    """Reads content from a file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        logging.error("File not found: %s", file_path)
        print("Error: The file was not found.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        print("An unexpected error occurred while reading the file.")

def calculate_division(numerator, denominator):
    """Performs division and handles errors."""
    try:
        result = numerator / denominator
        print(f"The result is {result}")
    except ValueError as e:
        logging.error("Invalid value provided: %s", e)
        print("Error: Invalid value. Please enter numeric values.")
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero: %s", e)
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        print("An unexpected error occurred during division.")

# Test the functions
file_path = "nonexistent_file.txt"  # This will raise FileNotFoundError
read_file(file_path)

# This will raise ValueError or ZeroDivisionError based on the input
try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))
    calculate_division(numerator, denominator)
except ValueError:
    logging.error("Invalid input type for numerator or denominator.")
    print("Error: Please enter a valid number.")
