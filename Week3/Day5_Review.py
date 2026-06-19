import csv, json, os
from datetime import datetime

# 1. Read raw data (CSV)
# 2. Transform it (filter, calculate, format)
# 3. Save output (JSON) with a timestamped filename
# 4. Log what happened (print with datetime)

def run_pipeline(input_file, output_folder):
    """
    Reads a CSV, transforms the data,
    saves results as a timestamped JSON file.
    """
    # Step 1 — Read
    with open(input_file, "r", encoding="utf-8") as f:
        data = list(csv.DictReader(f))

    # Step 2 — Transform
    results = [row for row in data if int(row["population"]) > 1000000]

    # Step 3 — Save
    os.makedirs(output_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"report_{timestamp}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # Step 4 — Log
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Pipeline done — {len(results)} records saved to {output_path}")


run_pipeline("colombian_cities.csv", "week3_output")