"""
Colombian cities data validator.
Reads a CSV, validates every row, logs errors,
saves valid rows to JSON and invalid rows to a separate log.
"""

# 1. Custom exceptions: InvalidPopulationError, InvalidSalaryError, MissingFieldError
# 2. validate_row(row) — raises the appropriate exception
# 3. clean_row(row) — defensive cleaning before validation
# 4. run_validator(input_csv, output_folder):
#    - reads the CSV
#    - cleans and validates each row
#    - saves valid rows to valid_cities.json
#    - saves error log to errors_TIMESTAMP.json
#    - prints summary: X valid, Y invalid, Z skipped

import csv, json, os
from datetime import datetime

#1
class DataValidationError(Exception):
    """Raise data when data doesn't meet validation requirements."""
    pass

class InvalidPopulationError(DataValidationError):
    """Raise when population is invalid"""
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        super().__init__(f"Invalid population {value}: {reason}")

class InvalidSalaryError(DataValidationError):
    """Raise when population is invalid"""
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason
        super().__init__(f"Invalid salary {value}: {reason}")

class MissingFieldError(DataValidationError):
    """Raise when a required field is missing"""
    pass
#2
def validate_city(row):
    """Validate is the field is missing"""
    if not row.get("city"):
        raise MissingFieldError("There is no city")
    if not row.get("department"):
        raise MissingFieldError("There is no department")
    if not row.get("population"):
        raise MissingFieldError("There is no population")
    if not row.get("avg_salary_cop"):
        raise MissingFieldError("There is no salary")

    """Verify the population is greater than 0"""
    if float(row["population"]) <= 0:
        raise InvalidPopulationError(row["population"], "must be greater than 0")

    """Verify that salary is greater than 0"""
    if float(row["avg_salary_cop"]) <= 0:
        raise InvalidSalaryError(row["avg_salary_cop"], "must be greater than 0")

    return True

#3
def safe_convert_salary_and_population(value, default=0):
    """Safely convert salary and population into float"""
    try:
        result = float(str(value).replace(",","").strip())
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default

def clean_city(row):
    """Clean the city row"""
    return {
        "city": str(row.get("city")).strip() or "Unknown",
        "department": str(row.get("department")).strip() or "Unknown",
        "population": safe_convert_salary_and_population(row.get("population"), default=0),
        "avg_salary_cop": safe_convert_salary_and_population(row.get("avg_salary_cop"), default=0),
    }

def log_error(error_type, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"ERROR: {timestamp}: {error_type}: {error}"

#4
def run_validator(input_file, output_folder):
    #4.1 Read the CSV
    with open(input_file, "r", encoding="utf-8-sig") as csvfile:
        raw_data = list(csv.DictReader(csvfile))

    #4.2 cleans and validates each row
    data = []
    error_data = []
    for row in raw_data:
        try:
            validate_city(row)
            cleaned = clean_city(row)
            data.append(cleaned)
        except Exception as e:
            print(f"ROW: {row['city']} → ERROR: {e}")
            error_data.append(log_error("Clean Error", e))

    #4.3 Save json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(output_folder, exist_ok=True)

    output_path_data = os.path.join(output_folder, f"report_data_project_week4_{timestamp}.json")
    with open(output_path_data, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

    output_path_error = os.path.join(output_folder, f"report_error_project_week4_{timestamp}.json")
    with open(output_path_error, "w", encoding="utf-8") as outfile:
        json.dump(error_data, outfile, indent=4, ensure_ascii=False)

    #4.4 log
    print(f"[{datetime.now().strftime("%H:%M:%S")}] Pipeline done\n"
          f"Valid cities: {len(data)}\n"
          f"Not valid cities: {len(error_data)}\n"
          f"Total read: {len(raw_data)}\n")

run_validator("week3_day1_colombian_cities_project.csv", "week4_output")