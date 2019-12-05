from nltk.tokenize import sent_tokenize
import itertools

# Defines the lines function - splits strings based on \n, then iterates through a matching with b and appening if there is a match (NB sets to prevent duplicates)


def lines(a, b):
    same = []
    a = set(a.splitlines())
    b = set(b.splitlines())
    for x in a:
        if x in b:
            same.append(x)
    return same

# Similar to above for sentences; uses tokenize to split based on sentence, sets again for duplicates


def sentences(a, b):
    same = []
    a = set(sent_tokenize(a))
    b = set(sent_tokenize(b))
    for x in a:
        if x in b:
            same.append(x)
    return same

# helper function for substrings - uses set and iterates though the string, adding substrings of length n for an input k


def extractSubstrings(k, n):
    lst = set()
    for i in range((len(k) - n) + 1):
        lst.add(k[i:i + n])
    return lst

# similar to above - calls helper function to get a set of each of the substrings in a and b (prevents duplicates) then iterates through the a set and appends a list if a in b


def substrings(a, b, n):
    res = []
    aLst = extractSubstrings(a, n)
    bLst = extractSubstrings(b, n)
    for x in aLst:
        if x in bLst:
            res.append(x)
    return res
