from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(now)                          # 2024-06-13 10:45:23.123456
print(now.strftime("%d/%m/%Y"))     # 13/06/2024
print(now.strftime("%B %d, %Y"))    # June 13, 2024

# Parse a date string → datetime object
date_str = "2024-01-15"
date = datetime.strptime(date_str, "%Y-%m-%d")
print(date.year)   # 2024
print(date.month)  # 1

# Date arithmetic
today = datetime.now()
in_30_days = today + timedelta(days=30)
days_since = today - datetime(2024, 1, 1)
print(f"Days since Jan 1: {days_since.days}")

# Practical: timestamp a filename
timestamp = now.strftime("%Y%m%d_%H%M%S")
filename = f"report_{timestamp}.csv"
print(filename)  # report_20240613_104523.csv

#EXERCISE
"""
You have a list of Colombian public holidays as strings: ["2024-01-01", "2024-01-08", "2024-03-25", 
"2024-05-01", "2024-06-03"]. 1) Parse them into datetime objects, 2) print each one formatted as "Monday, 
January 01 2024", 3) calculate how many days apart each consecutive holiday is, and find which gap is the 
longest.
"""
holidays = [
    "2024-01-01",
    "2024-01-08",
    "2024-03-25",
    "2024-05-01",
    "2024-06-03"
]
# 1
parsed_days = [datetime.strptime(d, "%Y-%m-%d") for d in holidays]
# 2
date_format = [d.strftime("%A, %B %d %Y") for d in parsed_days]
print(date_format)
# 3
days_apart = [parsed_days[i+1]-parsed_days[i] for i in range(len(parsed_days)-1)]
index_max = days_apart.index(max(days_apart))
max_day = days_apart[index_max].days
print(f"The most separated days are between {date_format[index_max]} and {date_format[index_max+1]}: {max_day} days apart.")
