def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_nth_fibonacci(n):
    fib = fibonacci()
    for _ in range(n):
        num = next(fib)
    return num

# Example: Get the 15th Fibonacci number
print(get_nth_fibonacci(15))  # Output: 377
