#Challenge -> Read numbers from a file and handle errors gracefully

file_path = "myfile.txt" # this works only if myfile.txt is on same folder

with open(file_path) as f: # 'as' gives alias to a variable
    line = f.read()
    words = line.split() # Split() prevents counting letters as words.

    for word in words:
        try:
            num = float(word) # Selecting float datatypes only from pool of words in our text file.
            print("Number found:", num)

        except:
            pass  # to ignore anything that's not number(our main logic)     
