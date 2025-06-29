#- Calculate the area of a rectangle using user-input length and width

a = float(input('Enter the length of the rectangle: '))
b = float(input('Enter the width of the rectangle: '))

# Function to calculate the area of a rectangle
def area_of_rectangle(a,b):
    area = a * b
    return area

#printing the result for upto two decimal places
print(f'The area of the rectangle is {round(area_of_rectangle(a,b),2)} square units.')
