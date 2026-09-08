from datetime import datetime, date
def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age
def days_between_dates(date1, date2):
    difference = date2 - date1
    return abs(difference.days)
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
def get_day_of_week(input_date):
    return input_date.strftime("%A")
def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            "Please use YYYY-MM-DD."
        )
