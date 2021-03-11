from datetime import date

from Bookkeeping.application.db.people import get_employees
from Bookkeeping.application.salary import calculate_salary

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    today = date.today()
    print(f"Today's date: {today}")
