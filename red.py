#!/usr/bin/python2

"""words=file("aa.txt", "r").read().split() #read the words into a list.
uniqWords = sorted(set(words)) #remove duplicate words and sort
for word in uniqWords:
    print words.count(word), word
"""
import sys

p=sys.stdin.read().split("\n")
uniqword=sorted(set(p))
for word in uniqword:
	print p.count(word),word

