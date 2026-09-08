from calculations import (
    calculate_basic_salary,
    calculate_hra,
    calculate_da,
    calculate_bonus,
    calculate_tax,
    calculate_net_salary
)

from validators import (
    validate_salary,
    validate_experience,
    InvalidSalaryError,
    InvalidExperienceError
)
employee = {
    "name": "Ashmita",
    "basic_salary": 100000,
    "experience": 1
}
try:
    validate_salary(employee["basic_salary"])
    validate_experience(employee["experience"])
    basic_salary = calculate_basic_salary(employee["basic_salary"])
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    bonus = calculate_bonus(
        basic_salary,
        employee["experience"]
    )
    gross_salary = basic_salary + hra + da + bonus
    tax = calculate_tax(gross_salary)
    net_salary = calculate_net_salary(gross_salary, tax)
    print("Employee Name:", employee["name"])
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Bonus:", bonus)
    print("Tax:", tax)
    print("Net Salary:", net_salary)
except InvalidSalaryError as e:
    print("Salary Error:", e)
except InvalidExperienceError as e:
    print("Experience Error:", e)


OUTPUT:

Employee Name: Ashmita
Basic Salary: 100000
HRA: 20000.0
DA: 10000.0
Bonus: 2000.0
Tax: 26400.0
Net Salary: 105600.0

If Input set is:
employee = {
    "name": "Ashmita",
    "basic_salary": -100000,
    "experience": 1
}

then OUTPUT will be:
Salary Error: Salary must be greater than 0
