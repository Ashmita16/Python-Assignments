from utils import (
    calculate_age,
    days_between_dates,
    is_leap_year,
    get_day_of_week,
    parse_date
)
try:
    dob_input = input("Enter Date Of Birth (YYYY-MM-DD): ")

    dob = parse_date(dob_input)

    age = calculate_age(dob)
    day = get_day_of_week(dob)

    print("Age:", age)
    print("Day:", day)
    print("Leap Year:", is_leap_year(dob.year))
except ValueError as e:
    print("Error:", e)

OUTPUT:
Enter Date Of Birth (YYYY-MM-DD): 2004-01-16
Age: 22
Day: Friday
Leap Year: True
