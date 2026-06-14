import json
"""
# Python dict → JSON file
data = {
    "report": "Colombian cities",
    "year": 2024,
    "cities": [
        {"name": "Bogotá", "population": 8000000, "capital": True},
        {"name": "Bucaramanga", "population": 600000, "capital": False},
    ]
}

with open("week3_day2_cities_report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# JSON file → Python dict
with open("week3_day2_cities_report.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["report"])       # Colombian cities
print(loaded["cities"][0])    # first city dict
for city in loaded["cities"]:
    print(f"{city['name']}: {city['population']:,}")
"""
#EXERCISE
"""
Create a JSON file called departments.json with at least 4 Colombian departments. Each department 
should have: name, capital, population, cities (list). Write it to disk, read it back, and print a 
summary showing the department name, its capital, and how many cities it has.
"""
departments = {
    "report": "Colombian Departments",
    "created_at": "2024-06-13",
    "departments": [
        {
            "name": "Antioquia",
            "capital": "Medellín",
            "population": 6700000,
            "cities": ["Medellín", "Bello", "Itagüí", "Envigado"]
        },
        {
            "name": "Santander",
            "capital": "Bucaramanga",
            "population": 2200000,
            "cities": ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
        },
        {
            "name": "Valle del Cauca",
            "capital": "Cali",
            "population": 4500000,
            "cities": ["Cali", "Palmira", "Buenaventura", "Tuluá"]
        },
        {
            "name": "Atlántico",
            "capital": "Barranquilla",
            "population": 2500000,
            "cities": ["Barranquilla", "Soledad", "Malambo", "Sabanalarga"]
        },
    ]
}
#1 write it to disk
with open("week3_day2_departments_report.json", "w", encoding="utf-8") as f:
    json.dump(departments, f, indent=4, ensure_ascii=False)
#2 read it back
with open("week3_day2_departments_report.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
#3 print a summary showing the department name, its capital, and how many cities it has
print(loaded["report"])
for dept in loaded["departments"]:
    print(f"{dept['name']} - {dept['capital']} — Pop: {dept['population']:,} - Cities:{len(dept['cities'])}")

