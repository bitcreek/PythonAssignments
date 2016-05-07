"""9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

import re

# ------------------------------------------------
# Create a dictionary from given input file and
# count number of times email address appears.
# ------------------------------------------------
def createDictionary(fh):
    dictionary = dict()
    for line in fh:
        if not line.startswith("From "):
            continue
        else:
            line = line.rstrip()
            x = line.split(" ")
            email =  x[1]
            if email in dictionary:
                dictionary[email] += 1
            else:
                dictionary[email] = 1
    return dictionary

# ------------------------------------------------
# Find out the maximum key in given dictionary.
# ------------------------------------------------
def max(dictionary):
    max = None
    highest = None
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    highest = key
    return highest

# ---------------- MAIN ------------------------
#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
emailDictionary = createDictionary(fh)
key = max(emailDictionary)
print key, emailDictionary[key]