import os
import shutil
"""
# Current working directory
print(os.getcwd())

# Create a folder if it doesn't exist
folder = "week3_day3_data_output"
if not os.path.exists(folder):
    os.makedirs(folder)

# Build a path safely (works on Windows AND Mac/Linux)
file_path = os.path.join(folder, "week3_day3_results.csv")
print(file_path)  # data_output/results.csv or data_output\results.csv

# Creating the CSV
with open(file_path, "w", newline="", encoding="utf-8-sig") as f:
    f.write("city,population\n")
    f.write("Bogotá,8000000\n")
    f.write("Medellín,2500000\n")
print(f"File created at: {file_path}")

# List all files in a folder
files = os.listdir(folder)
print(files)

# List only CSV files in a folder. "." means the folder where the script is located
csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]
print(csv_files)

# Check if a file exists before opening it
if os.path.exists("week3_day1_colombian_cities.csv"):
    print("File found!")
else:
    print("File not found")
"""
#EXERCISE
"""
Write a script that: 1) creates a folder called week3_output/ if it doesn't exist, 2) saves your 
colombian_cities.csv from Day 1 inside that folder using os.path.join(), 3) lists all files in 
that folder and prints them, 4) checks if a specific file exists before trying to open it.
"""
# 1
folder = "week3_day3_data_output"
if not os.path.exists(folder):
    os.makedirs(folder)
# 2
src = "week3_day1_colombian_cities.csv"
dst = os.path.join(folder, "week3_day1_colombian_cities.csv")
shutil.copyfile(src, dst)
print(f"File copied at: {dst}")
# 3
files1 = os.listdir(folder)
print(files1)
# 4
if os.path.exists("week3_day1_colombian_cities.csv"):
    print("File found!")
else:
    print("File not found")