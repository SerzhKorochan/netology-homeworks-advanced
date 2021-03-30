from Decorators.logger import logger


@logger('logs/important_logs/')
def calculate_salary():
    print('Salary has been calculated.')
