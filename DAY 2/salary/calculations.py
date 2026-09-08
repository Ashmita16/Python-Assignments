def calculate_basic_salary(basic_salary):
    return basic_salary
def calculate_hra(basic_salary):
    return basic_salary * 0.20
def calculate_da(basic_salary):
    return basic_salary * 0.10
def calculate_bonus(basic_salary, experience):
    if experience >= 5:
        return basic_salary * 0.10
    elif experience >= 2:
        return basic_salary * 0.05
    else:
        return basic_salary * 0.02
def calculate_tax(gross_salary):
    if gross_salary > 100000:
        return gross_salary * 0.20
    elif gross_salary > 50000:
        return gross_salary * 0.10
    else:
        return 0
def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax
