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
