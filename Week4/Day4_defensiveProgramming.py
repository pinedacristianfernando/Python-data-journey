def safe_convert_salary(value, default=0):
    """Safely converts a value to float salary."""
    try:
        result = float(str(value).replace(",", "").strip())
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default


def clean_city_row(row):
    """Cleans and validates a single city row."""
    return {
        "city": str(row.get("city", "")).strip() or "Unknown",
        "population": safe_convert_salary(row.get("population"), default=0),
        "avg_salary_cop": safe_convert_salary(row.get("avg_salary_cop"), default=0),
        "department": str(row.get("department", "")).strip() or "Unknown",
    }

# Messy real-world data
messy_data = [
    {"city": "Bogotá ", "population": "8,000,000", "avg_salary_cop": "4500000"},
    {"city": "", "population": None, "avg_salary_cop": "abc"},
    {"city": "Medellín", "population": "2500000", "avg_salary_cop": ""},
]

cleaned = [clean_city_row(row) for row in messy_data]
for row in cleaned:
    print(row)

#EXERCISE
"""
Take your pipeline from Week 3 Day 5 and make it defensive. Add a clean_row() function that handles: 
missing fields, values that can't be converted to numbers, empty strings, and extra whitespace. The 
pipeline should never crash — it should skip bad rows and log how many were skipped.
"""
import csv, json, os
from datetime import datetime

# Values that can't be converted to numbers
def safe_convert_salary(value, default=0):
    """Safely converts a value to float salary."""
    try:
        result = float(str(value).replace(",", "").strip())
        return result if result > 0 else default
    except (ValueError, TypeError):
        return default

# Missing fields, empty strings, and extra whitespace
def clean_city_row(row):
    """Cleans and validates a single city row."""
    return {
        "city": str(row.get("city", "")).strip() or "Unknown",
        "population": safe_convert_salary(row.get("population"), default=0),
        "avg_salary_cop": safe_convert_salary(row.get("avg_salary_cop"), default=0),
        "department": str(row.get("department", "")).strip() or "Unknown",
    }

def run_pipeline(input_file, output_folder):
    """
    Reads a CSV, transforms the data,
    saves results as a timestamped JSON file.
    """
    # Step 1 — Read
    with open(input_file, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    # Step 2 — Transform
    valid_results = []
    skipped = 0
    for row in data:
        try:
            cleaned = clean_city_row(row)
            if cleaned["population"] > 1000000:
                valid_results.append(cleaned)
        except Exception as e:
            skipped += 1
            print(f"[WARNING] Skipped row: {e}")

    # Step 3 — Save
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"report_{timestamp}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(valid_results, f, indent=4, ensure_ascii=False)

    # Step 4 — Log
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Pipeline done\n"
          f"Total rows read:   {len(data)}\n"
          f"Valid rows saved:  {len(valid_results)}\n"
          f"Rows skipped:      {skipped}\n"
          f"Output:            {output_path}")

run_pipeline("week3_day1_colombian_cities.csv", "week4_output")