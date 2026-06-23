def process_salary(salary_str):
    """Converts a salary string to float and validates it."""
    try:
        salary = float(salary_str)

        if salary < 0:
            raise ValueError(f"Salary cannot be negative: {salary}")
        if salary > 50_000_000:
            raise ValueError(f"Salary seems too high: {salary}")

    except ValueError as e:
        print(f"Invalid salary: {e}")
        return None

    else:
        # Only runs if no exception occurred
        print(f"Salary validated: ${salary:,.0f}")
        return salary

    finally:
        # Always runs — great for logging
        print("process_salary() completed")


process_salary("3500000")    # valid
process_salary("abc")        # ValueError from float()
process_salary("-100000")    # ValueError we raised
process_salary("99999999")   # ValueError we raised

#EXCERSISE
"""
Write a function validate_city_data(row) that receives a dict with city data and raises a ValueError if: 
population is negative, avg_salary_cop is zero or missing, or city name is empty. Use else to print a 
success message and finally to log that the function ran. Test it with valid and invalid data.
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
valid = {
    "city": "Manizales",
    "population": 120000,
    "avg_salary_cop": 3400000,
    "department": "Caldas"
}

def validate_city_data(city_information):
    try:
        population = city_information["population"]
        salary = city_information["avg_salary_cop"]
        if population < 0 :
            raise ValueError(f"Population cannot be negative: {population}")
        if salary <= 0:
            raise ValueError(f"Salary can not be negative: {salary}")
        if salary is None:
            raise ValueError(f"There is no salary: {salary}")
        if city_information["city"] is None:
            raise ValueError(f"City cannot be empty: {city_information['city']}")

    except ValueError as e:
        print(f"Invalid city information: {e}")

    else:
        print(f"City validated: {city_information}")

    finally:
        print("validate_city_data() completed")

validate_city_data(invalid_population)
validate_city_data(invalid_salary)
validate_city_data(invalid_name)
validate_city_data(valid)




