from faker import Faker
import csv
import datetime
import random

fake = Faker()

def generate_employee_data(num_employees=100, output_file="employee_data.csv"):
    """
    Generates dummy employee data, including password and salary,
    and saves it to a CSV file.

    Args:
      num_employees: The number of employee records to generate.
      output_file: The name of the output CSV file.
    """

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "date_of_birth",
            "address",
            "job_title",
            "department",
            "hire_date",
            "salary",
            "gender",
            "nationality",
            "password" # Added Password field
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_employees):
            birth_date = fake.date_of_birth(minimum_age=22, maximum_age=60)
            hire_date = fake.date_between(start_date='-10y', end_date='today')
             # Generate a password (simple string). You can generate more complex strings if desired but not actual hash passwords

            writer.writerow({
                "employee_id": fake.unique.random_int(min=1000, max=9999),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "phone_number": fake.phone_number(),
                "date_of_birth": birth_date.strftime("%Y-%m-%d"),
                "address": fake.address(),
                "job_title": fake.job(),
                "department": random.choice(["Sales", "Marketing", "Engineering", "Human Resources", "Finance"]),
                "hire_date": hire_date.strftime("%Y-%m-%d"),
                "salary": round(random.uniform(40000, 150000),2),  # added salary
                "gender": random.choice(["Male", "Female", "Other"]),
                "nationality": fake.country(),
                "password": fake.password(length=10, special_chars=False, upper_case=True, digits=True) #Generate dummy password
            })

    print(f"Dummy employee data generated and saved to: {output_file}")

if __name__ == "__main__":
    generate_employee_data(num_employees=150) # Generates 150 employees

    
