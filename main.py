import datetime
from application.db import people
from application import salary

if __name__ == '__main__':
    print(datetime.date.today())
    people.get_employees()
    salary.calculate_salary()
