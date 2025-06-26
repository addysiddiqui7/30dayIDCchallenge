# Validate gmail addresses using regex.

import re

#here we assign the user to do his own input
user_input = input("Enter your gmail:")

# typical pattern to find gmail, here the $ sign indicates to check on end part.
pattern = r"@gmail.com$"
match = re.search(pattern, user_input)

# Basic logic again
if match:
    print('The email is accepted.')
else:
    print('Error! Wrong email.')
