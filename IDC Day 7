#create our text file
f = open('file.txt','a')
f.close()

#open our text file and write contents in it
f = open('file.txt','w')
f.write('Hello, This is a sample text file with certain words of certain limit')
f.close()

#open our text file in read only view and store the contents in an object 'content'
with open('file.txt','r') as f:
    content = f.read()

#define an object 'words' having contents split() in words; 
# If we don't use split then it will count letters as words
words = content.split()

#print our length of words
word_count = len(words)
print('Total words in our text file are:',word_count)
