from package.application import people, salary
from datetime import datetime

if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    print(datetime.now())