# Define custom exceptions
class DataValidationError(Exception):
    """Raised when data doesn't meet validation requirements."""
    pass

class InvalidSalaryError(DataValidationError):
    """Raised when a salary value is invalid."""
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        super().__init__(f"Invalid salary {value}: {reason}")

class MissingFieldError(DataValidationError):
    """Raised when a required field is missing."""
    pass


# Using custom exceptions
def validate_employee(data):
    if "name" not in data or not data["name"]:
        raise MissingFieldError("Field 'name' is required")

    salary = data.get("salary_cop", 0)
    if salary <= 0:
        raise InvalidSalaryError(salary, "must be greater than 0")
    if salary > 50_000_000:
        raise InvalidSalaryError(salary, "exceeds maximum allowed")

    return True

try:
    validate_employee({"name": "Ana", "salary_cop": -500})
except InvalidSalaryError as e:
    print(f"Salary error: {e.reason} (value: {e.value})")
except MissingFieldError as e:
    print(f"Missing field: {e}")

#EXERCISE
"""
Create 3 custom exceptions for your Colombian cities pipeline: InvalidPopulationError, InvalidCityNameError,
 and MissingColumnError. Write a function validate_city_row(row) that raises the appropriate exception 
 for each case. Test with at least 4 different invalid rows.
"""
# Invalid — negative population
invalid_population = {
    "city": "Medellín",
    "population": -500000,
    "avg_salary_cop": 3800000,
    "department": "Antioquia"
}

# Invalid — salary is zero
invalid_salary = {
    "city": "Cali",
    "population": 2200000,
    "avg_salary_cop": 0,
    "department": "Valle del Cauca"
}

# Invalid — empty city name
invalid_name = {
    "city": "",
    "population": 1200000,
    "avg_salary_cop": 3400000,
    "department": "Atlántico"
}

# Invalid — empty city name
invalid_column = {
    "city": "Manizales",
    "avg_salary_cop": 3400000,
    "department": "Caldas"
}

class DataValidationErrorExercise(Exception):
    """Raised when data doesn't meet validation requirements."""
    pass

class InvalidPopulationError(DataValidationErrorExercise):
    """Raised when a population is invalid."""
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        super().__init__(f"Invalid population {value}: {reason}")

class InvalidSalaryError(DataValidationErrorExercise):
    """Raised when a salary is invalid."""
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        super().__init__(f"Invalid salary {value}: {reason}")

class InvalidCityNameError(DataValidationErrorExercise):
    """Raised when a city name is invalid."""
    pass

class MissingColumnError(DataValidationErrorExercise):
    """Raised when a required field is missing."""
    pass

def validate_city_row(row):
    """Verifies that the columns exist"""
    if row.get("city") is None:
        raise MissingColumnError("There is no city in this row")
    if row.get("population") is None:
        raise MissingColumnError("There is no population in this row")
    if row.get("avg_salary_cop") is None:
        raise MissingColumnError("There is no salary in this row")
    if row.get("department") is None:
        raise MissingColumnError("There is no department in this row")

    """Verifies that the city name is not empty"""
    if not row["city"]:
        raise InvalidCityNameError("Field 'city' is required")

    """Verifies the population is greater than zero"""
    if float(row["population"]) <= 0:
        raise InvalidPopulationError(row["population"], "must be greater than 0")

    """Verifies the salary is greater than zero"""
    if float(row["avg_salary_cop"]) <= 0:
        raise InvalidSalaryError(row["avg_salary_cop"], "must be greater than 0")

    return True

try:
    validate_city_row(invalid_population)
except InvalidPopulationError as e:
    print(f"Population error: {e}")

try:
    validate_city_row(invalid_salary)
except InvalidSalaryError as e:
    print(f"Salary error: {e}")

try:
    validate_city_row(invalid_name)
except InvalidCityNameError as e:
    print(f"City name error: {e}")

try:
    validate_city_row(invalid_column)
except MissingColumnError as e:
    print(f"Column missing: {e}")


