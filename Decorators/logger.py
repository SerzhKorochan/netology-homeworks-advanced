def logger(path='logs/'):

    def actual_decorator(func):
        import datetime

        def save_logs(*args, **kwargs):
            log = {
                'current_datetime': datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),
                'name': func.__name__,
                'args': [args, kwargs],
                'return_value': func(*args, **kwargs)
            }
            file_path = path + log['current_datetime'] + '.txt'

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(str(log))

            return log.get('return_value')

        return save_logs
    return actual_decorator
