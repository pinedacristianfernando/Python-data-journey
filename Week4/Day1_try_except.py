import csv
"""
# Without error handling — crashes if file doesn't exist
with open("data.csv", "r") as f:
    data = f.read()  # FileNotFoundError!

# With try/except — handles the error gracefully
try:
    with open("data.csv", "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))
    print(f"Loaded {len(data)} rows")

except FileNotFoundError:
    print("Error: file not found. Check the path.")

except Exception as e:
    print(f"Unexpected error: {e}")

# Multiple except blocks — handle different errors differently
try:
    value = int("not_a_number")
except ValueError as e:
    print(f"Could not convert: {e}")
except TypeError as e:
    print(f"Wrong type: {e}")
"""
#EXERCISE
"""
Write a function load_csv(filepath) that tries to open and read a CSV file. Handle at least 3 error 
types: FileNotFoundError, PermissionError, and a general Exception. Test it by calling it with a 
file that exists and one that doesn't.
"""
def load_csv(file):
    try:
        with open(file, "r") as f:
            data = list(csv.DictReader(f))
            print(f"Loaded {len(data)} rows successfully")
            return data
    except FileNotFoundError as e:
        print(f"Error: {e}. file not found. Check the path.")
        return None
    except PermissionError as e:
        print(f"Error: {e} there is a permission error.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test with a file that exists
load_csv("Week3/week3_day1_colombian_cities.csv")

# Test with a file that doesn't exist
load_csv("fake_file.csv")




