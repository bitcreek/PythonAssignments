# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt


#fname = raw_input("Enter file name: ")
fname = "romeo.txt"
fh = open(fname)
lst = list()
uniqueWords = []
for line in fh:
    words =  (line.rstrip()).split(" ")
    for word in words:
        if word in uniqueWords:
            continue
        else:
            uniqueWords.append(word)
uniqueWords.sort()
print uniqueWords
print len(uniqueWords)

abc = "sabina"
print len(abc)

x = range(5)
print x;
