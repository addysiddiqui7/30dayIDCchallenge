import time

# ✨ Our decorator function
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # call the original function
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def summation(a,b):
    return a + b

sum = summation(5, 10)
print(f'The sum is:{sum}')

