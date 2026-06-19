"""
Colombian cities data pipeline.
Reads raw CSV, enriches it with calculations,
saves a timestamped JSON report, logs each step.
"""

# 1. Read week3_day1_colombian_cities.csv
# 2. Add calculated columns:
#    - salary_usd = avg_salary_cop / 4200
#    - category = "major" if population > 1M else "minor"
# 3. Filter: only cities where salary_usd > 500
# 4. Save filtered results to week3_output/report_TIMESTAMP.json
# 5. Print a summary: total cities read, cities after filter,
#    output filename, timestamp of run

import csv, json, os
from datetime import datetime

def run_pipeline(input_file, output_folder):
    """
    Reads a CSV, transforms the data,
    saves results as a timestamped JSON file.
    """
    # Step 1 — Read
    with open(input_file, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    # Step 2 — Transform
    for row in data:
        row["salary_usd"] = round(float(row["avg_salary_cop"]) / 4200, 2)
        row["category"] = "major" if int(row["population"]) > 100000 else "minor"

    results = [row for row in data if int(row["salary_usd"]) > 800]

    # Step 3 — Save
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"report_{timestamp}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # Step 4 — Log
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Pipeline done\n"
          f"Cities read: {len(data)}\n"
          f"Cities after filer: {len(results)}\n"
          f"Records saved to {output_path}")

run_pipeline("week3_day1_colombian_cities.csv", "week3_day3_data_output")