#Python program to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for i in range (2, int(n**0.5) +1):
#applying logic of prime number and it's devisibility and range (from 2 to (square root of n) + 1)
        if n % i == 0:
            return False
        else:
            return True
        
# Test the function with an example
num = int(input("Enter a number:"))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
