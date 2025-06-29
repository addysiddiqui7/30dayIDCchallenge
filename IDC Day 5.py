#- Write a function that computes the sum and average of a list of numbers
list1 = [1,2,3,4,5]

def sum_and_average(list1):
    print(f'The sum of the list is {sum(list1)} and the average is {sum(list1)/len(list1)}')        ####Python has built in sum().

# Test the function with an example
print(sum_and_average(list1))
