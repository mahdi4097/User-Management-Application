from functools import wraps
import time
from datetime import datetime
import sqlite3


def confirmation_decorator(func):
    last_switch_time = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_switch_time

        current_time = time.time()
        if current_time - last_switch_time >= 60:
            args[0].__dict__['main_view'].switch_frame('critical_activity_confirmation')
            last_switch_time = current_time

        return func(*args, **kwargs)

    return wrapper


def performance_logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        call_dateteme = datetime.now()
        start_time = time.time()
        function_result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        with sqlite3.connect('UserManagementDB.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                '''
                            INSERT INTO PerformanceLogger (
                                                 function_name,
                                                 call_datetime,
                                                 execution_time
                                             )
                            VALUES (?,?,?);
                            ''', [function_name, call_dateteme, execution_time]
                )

            connection.commit()

        return function_result

    return wrapper
