"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Note that the autograder does not have support for the sorted() function.
"""

import re

# -------------------------------------------------
# Extract data from file and Create Dictionary
# ------------------------------------------------
def createDictionary(fh):
    dictionary = dict()
    for line in fh:
        x = re.findall('^From .* ([0-9][0-9]):',line)
        if len(x) > 0:
            y = (str(x).strip('[]')).strip('\'')
            if y in dictionary:
               dictionary[y] += 1
            else:
               dictionary[y] = 1
    return dictionary

# ------------------------------------------------
# Items in dictionary are in no particular order,
# whereas tuple is a key-value pair and can be
# sorted. Sort the given dictionary and print.
# ------------------------------------------------
def showDictionary(dictionary):
   tuples = dictionary.items()
   tuples.sort()

   for key,val in tuples :
        print key,val

# ---------------- MAIN ------------------------
#fname = raw_input("Enter file:")
fname = "mbox-short.txt"
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
hourDistribution = createDictionary (fh)
showDictionary(hourDistribution)
