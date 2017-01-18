__author__ = 'jay'

'''
A program that counts how many a’s, b’s, c’s etc. there are in the string The quick brown fox jumped over the lazy
dog. Case-fold the characters before counting; i.e., count the T in The as a t, just like a lower-case t. The program
displays the characters (a-z) and their counts. E.g., it should show that there are four o’s.
'''

s = "The quick brown fox jumped over the lazy dog"
s_lower = s.lower()

indx = 0
for c in s_lower:
    if c != " ":
        cntr = 1
        inner_indx = 0
        for checker in s_lower:
            if inner_indx != indx and c == checker:
                cntr += 1
            inner_indx += 1
        isAre = "is"
        if cntr > 1:
            isAre = "are"
        print("There %s %d %s" % (isAre, cntr, c))
    indx += 1
