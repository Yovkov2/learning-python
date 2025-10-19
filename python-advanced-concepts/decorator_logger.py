import time
from functools import wraps

def log_time(func):
    """Decorator that prints function name and execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__} with args {args}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f}s\n")
        return result
    return wrapper

@log_time
def slow_add(a, b):
    time.sleep(1)
    return a + b

@log_time
def greet(name):
    time.sleep(0.5)
    return f"Hello, {name}!"

print(slow_add(2, 3))
print(greet("Anna"))
