
''' A python programme to demonstrate
the use of clean code ethic'''


#a messy code for reversing a string
s="Addy"
r=""
for i in range(len(s)-1,-1,-1):r+=s[i] #range(start, stop, step)
print("rev:",r)


# A clean code for reversing a string
def reverse_string(s):
    """Reverses the input string."""
    return s[::-1]  # Slicing to reverse the string

s = "Addy"
reversed_s = reverse_string(s)

print("Reversed string:", reversed_s)




