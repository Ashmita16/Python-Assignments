class InvalidSalaryError(Exception):
    pass
class InvalidExperienceError(Exception):
    pass
def validate_salary(basic_salary):
    if basic_salary <= 0:
        raise InvalidSalaryError("Salary must be greater than 0")
def validate_experience(experience):
    if experience < 0:
        raise InvalidExperienceError("Experience cannot be negative")
