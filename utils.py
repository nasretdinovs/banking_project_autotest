from datetime import datetime


def fibonacci_for_date():
    current_date = datetime.now()
    n = current_date.day + 1
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n - 1]
