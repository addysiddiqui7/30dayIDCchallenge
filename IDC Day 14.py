#Challenge: Calculate Factorial of a number using recursion

#Defining a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1: # cuz the factorial of 0 and 1 is 1
        return 1
    else:
        return n * factorial(n - 1) # This is the recursive function that calls itself
    
# Main program to take user input and display the factorial
num = input("Enter a number to calculate its factorial: ")
num = int(num)
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
