#!/usr/bin/env python2

f=open('/root/Desktop/youtubedata/4.txt')
f1=open('/root/Desktop/youtubedata/n4.txt', 'a')

doIHaveToCopyTheLine=False
x=5
for line in f.readlines():
	x=len(line.split())
	if x>9 :
		f1.write(line)    		
		
f1.close()
f.close()

